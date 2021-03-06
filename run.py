from flask import Flask, render_template, url_for, redirect
from forms import RegisterForm, LoginForm
from datetime import date, datetime
from flask_moment import Moment


app = Flask(__name__)
app.config['SECRET_KEY'] = 'youwillneverguess!'
moment = Moment(app)

post = [ 
    { 
        'post-title' : '我的第一篇文章',
        'post-content' : '之後原先關注的片子跳出了上映播送的提醒-Ragnarök 諸神黃昏，觀看沒多久就有追下去的慾望，故事發生在有海盜傳奇歷史的挪威，加上北歐神話與漫威中的部分角色剛好也是主角，我喜歡。主場景在一個湖邊的小鎮內，有機會看到北歐峽谷地形，美不勝收的冰川，當然生活日常/環境/人與人間的相處也可一探，同時隱含部分環境保護，主角一家三口回到小鎮重新生活，本身是高中生，學校場景當然也不少，但北歐高中生的成熟度會讓人覺得這是大學生吧的錯覺。 諸神黃昏從字面上看起來很屌，其實並不熟悉，為此還惡補一下，是闡述北歐的神與巨人間的戰爭，是一場激烈的戰鬥不少神因此死亡，故名。時間到了現代，這場戰役是否結束了？抑或是以另一形勢在進行中，同時諸神黃昏所描述的世界未日也在進行中，冰川融化、毒害河流、魚類變異等等環保意識的梗也穿插其中。 如果對美劇太刻意演出靈異或超級英雄感到很膩，可試著看看，劇情安排並不會太誇張，藉由一連串小事件探索小時發生於故鄉與身上奇異事件的關連，雖然老婆嫌男主很不好看沒追，但沒關係還有其他人可以補分，就這樣我沉浸在北歐風景與神話當中，只可惜本劇只有短短6集，意猶未盡呀！！！ ',
        'post-date': 'April 10, 2020'
    },

    {
        'post-title' : '我的第二篇文章',
        'post-content' : '上看起來很屌，其實並不熟悉，為此還惡補一下，是闡述北歐的神與巨人間的戰爭，是一場激烈的戰鬥不少神因此死亡，故名。時間到了現代，這場戰役是否結束了？抑或是以另一形勢在進行中，同時諸神黃昏所描述的世界未日也在進行中，冰川融化、毒害河流、魚類變異等等環保意識的梗也穿插其中。 如果對美劇太刻意演出靈異或超級英雄感到很膩，可試著看看，劇情安排並不會太誇張，藉由一連串小事件探索小時發生於故鄉與身上奇異事件的關連，雖然老婆嫌男主很不好看沒追，但沒關係還有其他人可以補分，就這樣我沉浸在北歐風景與神話當中，只可惜本劇只有短短6集，意猶未盡呀！！！ 其實我已看了不少Netflix上的劇，很多一下子就追不下去，而Netflix近期也常不知什麼原因想砍就砍，這樣的做法已引來不少批評，像收視不錯的小鎮滋味(Santa Clarita Diet)、先見之明(The OA)、漫威相關，所以你喜歡可能也會被砍。 ',
        'post-date': 'May 11, 2020'
    },

    {
        'post-title' : '我的第三篇文章',
        'post-content' : '上看起來很屌，其實並不熟悉，為此還惡補一下，是闡述北歐的神與巨人間的戰爭，是一場激烈的戰鬥不少神因此死亡，故名。時間到了現代，這場戰役是否結束了？抑或是以另一形勢在進行中，同時諸神黃昏所描述的世界未日也在進行中，冰川融化、毒害河流、魚類變異等等環保意識的梗也穿插其中。 如果對美劇太刻意演出靈異或超級英雄感到很膩，可試著看看，劇情安排並不會太誇張，藉由一連串小事件探索小時發生於故鄉與身上奇異事件的關連，雖然老婆嫌男主很不好看沒追，但沒關係還有其他人可以補分，就這樣我沉浸在北歐風景與神話當中，只可惜本劇只有短短6集，意猶未盡呀！！！ 其實我已看了不少Netflix上的劇，很多一下子就追不下去，而Netflix近期也常不知什麼原因想砍就砍，這樣的做法已引來不少批評，像收視不錯的小鎮滋味(Santa Clarita Diet)、先見之明(The OA)、漫威相關，所以你喜歡可能也會被砍。 ',
        'post-date': 'May 11, 2020'
    },

    {
        'post-title' : '我的第四篇文章',
        'post-content' : '上看起來很屌，其實並不熟悉，為此還惡補一下，是闡述北歐的神與巨人間的戰爭，是一場激烈的戰鬥不少神因此死亡，故名。時間到了現代，這場戰役是否結束了？抑或是以另一形勢在進行中，同時諸神黃昏所描述的世界未日也在進行中，冰川融化、毒害河流、魚類變異等等環保意識的梗也穿插其中。 如果對美劇太刻意演出靈異或超級英雄感到很膩，可試著看看，劇情安排並不會太誇張，藉由一連串小事件探索小時發生於故鄉與身上奇異事件的關連，雖然老婆嫌男主很不好看沒追，但沒關係還有其他人可以補分，就這樣我沉浸在北歐風景與神話當中，只可惜本劇只有短短6集，意猶未盡呀！！！ 其實我已看了不少Netflix上的劇，很多一下子就追不下去，而Netflix近期也常不知什麼原因想砍就砍，這樣的做法已引來不少批評，像收視不錯的小鎮滋味(Santa Clarita Diet)、先見之明(The OA)、漫威相關，所以你喜歡可能也會被砍。 ',
        'post-date': 'May 11, 2020'
    }
]

@app.route("/")
def home():
    return render_template('index.html', name='Home page', getposts=post)

@app.route("/about")
def about():
    return render_template('about.html',name='關於')

@app.route("/login", methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.is_submitted() and form.validate():
        return redirect(url_for('home'))
    return render_template('login.html',name='登入', form=form)

@app.route("/register", methods=['GET','POST'])
def register():
    form = RegisterForm()
    return render_template('register.html',name='註冊',form=form)
    
if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port=5000);

