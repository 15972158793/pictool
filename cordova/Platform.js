var Platform = {
    //录屏功能
    gameRecorder:null,
    gameVideoUrl:"",

    /**
     * 开始录屏
     * @param time 
     */
    startGameRecord:function(time) {
        if(cc.sys.platform !== cc.sys.WECHAT_GAME) return;

        var self = this;
        if(self.gameRecorder == null){
            self.gameRecorder = wx.getGameRecorderManager();
            //录屏结束的时候获取到视频地址
            self.gameRecorder.onStop(function(res){
                self.gameVideoUrl = res.videoPath;
            });
        }
        self.gameRecorder.start({duration: time });
    },
     
    /**
     * 结束录屏
     */
    stopGameRecord:function() {
        if(cc.sys.platform !== cc.sys.WECHAT_GAME) return;
        
        var self = this;
        if(self.gameRecorder != null){
            self.gameRecorder.stop();
        }
    },

    /**
     分享录制的视频
    */
    shareRecordVideo:function(title,des){
        if(cc.sys.platform !== cc.sys.WECHAT_GAME) return;

        var self = this;
        wx.shareAppMessage({
            channel: 'video',  //指定为视频分享
            templateId:"35hcf13ga8hd2uno82",
            title: title,
            desc:des,
            extra: {
                videoPath:self.gameVideoUrl
            },
            success: () => {
                //分享回调
                console.log('录屏分享成功');
                //分享奖励，仅一次
                /*if (!this._isVideoShared) {
                    this._isVideoShared = true;
                    this.getGoldSuccess();
                }*/
            },
            fail: (e) => {
                console.log('录屏分享失败');
            }
        });
    }
};

window.MyPlatform = Platform;
