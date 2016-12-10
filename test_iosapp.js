var target = UIATarget.localTarget();  //UIATarget是最上层的类，表示真实设备或模拟器    

try{

    target.delay(3); //等待3秒，跳过开场动画

    UIALogger.logStart("test 1"); //第1个Case

    UIALogger.logMessage("开始第一个测试");

    var leftButton = target.frontMostApp().navigationBar().leftButton();  //取得导航栏的左侧按钮

    leftButton.tap(); //点击

    var techCell = target.frontMostApp().mainWindow().tableViews()[0].cells()["技术问答"];  //取得第一个cell

    if (techCell.isValid() && techCell.isVisible()) {

        UIALogger.logPass("find 技术问答");

    } else {

        UIALogger.logFail("cannot find 技术问答");

    }

    UIALogger.logStart("test 2"); //第2个Case

    UIALogger.logMessage("开始第二个测试"); 

    target.frontMostApp().mainWindow().buttons()[0].tap();

    target.delay(1); //等待动画结束

    target.frontMostApp().tabBar().buttons()["我"].tap();

    target.delay(1); //等待动画结束

    target.frontMostApp().mainWindow().tableViews()[1].cells()["消息"].tap();

    target.delay(1); //等待动画结束

    var loginButton = target.frontMostApp().mainWindow().buttons()["登录"];

    if(loginButton.isValid() && loginButton.isVisible()){ //如果登陆按钮有效且可见，则表示用户未登录，接下来尝试登陆

        var textField = target.frontMostApp().mainWindow().textFields()[0];

        var secureTextField = target.frontMostApp().mainWindow().secureTextFields()[0];

        textField.tap();

        textField.setValue("18856785678"); //输入用户名

        target.delay(0.5);

        secureTextField.tap();

        secureTextField.setValue("5678"); //输入密码

        target.delay(0.5);

        loginButton.tap();

        target.delay(3);

        if(loginButton.isValid() && loginButton.isVisible()){    

            UIALogger.logFail("登陆失败");

        }else{

            UIALogger.logPass("登陆成功");

        }

    }else{

        UIALogger.logPass("用户已经登陆");

    }

}catch(err){

    UIALogger.logError(err.toString());

}
