using System.Collections;
using System.Collections.Generic;
using UnityEngine;


public class bar : MonoBehaviour
{
    private const float CONFIGURED_BAR_SPEED = 0.09f;
    private float screenLeftCoordinate = 0.0f;
    private float screenRightCoordinate = 0.0f;

    private Camera mainCamera;
    private GameObject ball;

    private float ballWidth;
    private float ballHeight;
    private float barWidth;
    private float barHeight;

    // Start is called before the first frame update
    void Start()
    {
        //画面の左端と右端の座標を取得
        GameObject obj = GameObject.Find("Main Camera");
        ball = GameObject.Find("ball");
        mainCamera = obj.GetComponent<Camera>();

        ballWidth = ball.GetComponent<SpriteRenderer>().bounds.size.x;
        ballHeight = ball.GetComponent<SpriteRenderer>().bounds.size.y;
        barWidth = GetComponent<SpriteRenderer>().bounds.size.x;
        barHeight = GetComponent<SpriteRenderer>().bounds.size.y;

        screenLeftCoordinate = getScreenLeft();
        screenRightCoordinate = getScreenRight();

    }

    // Update is called once per frame
    void Update()
    {

        //FIXME:とりあえず画面の外には行かなくなったが
        //完全には止められていないし、毎フレームVectorクラスを生成しているのも気になる
        //加えてこのif-elseの羅列を何とかできないだろうか。
        if (transform.position.x < screenLeftCoordinate)
        {
            transform.position = new Vector3(screenLeftCoordinate, -3, 0);
            transform.Translate(0, 0, 0);
        } else if(transform.position.x > screenRightCoordinate)
        {
            transform.position = new Vector3(screenRightCoordinate, -3, 0);
            transform.Translate(0, 0, 0);
        }

        if (Input.GetKey(KeyCode.LeftArrow)){
            transform.Translate(-CONFIGURED_BAR_SPEED, 0, 0 );
        } else if (Input.GetKey(KeyCode.RightArrow))
        {
            transform.Translate(CONFIGURED_BAR_SPEED, 0, 0);
        }

        //FIXME:barクラスを見ると分かるが、かなり重複している
        //コリジョン専用のクラスを作っておいてそこから呼び出すようにしたほうがいいだろう

        Vector2 ballVector = ball.transform.position;
        Vector2 barVector = transform.position;

        

        bool checkFlag1 = ballVector.x <= barVector.x + barWidth;
        bool checkFlag2 = (barVector.x - (barWidth/2.0))<= ballVector.x + ballWidth;
        bool checkFlag3 = ballVector.y <= barVector.y + barHeight;
        bool checkFlag4 = barVector.y <= ballVector.y + ballHeight;


        if (checkFlag1 && checkFlag2 && checkFlag3 && checkFlag4)
        {
            GetComponent<AudioSource>().Play();
            ball.GetComponent<ball>().invertYVelocity();

        }
    }

    private float getScreenLeft()
    {
        Vector3 topLeft = mainCamera.ScreenToWorldPoint(Vector3.zero);
        return topLeft.x;
    }

    private float getScreenRight()
    {
        Vector3 bottomRight = mainCamera.ScreenToWorldPoint(new Vector3(Screen.width, Screen.height, 0.0f));
        return bottomRight.x;

    }
}
