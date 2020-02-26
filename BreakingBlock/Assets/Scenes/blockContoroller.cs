using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class blockContoroller : MonoBehaviour
{
    private GameObject ball;
    private GameObject blockGenerator;


    private float ballWidth;
    private float ballHeight;
    private float thisBlockWidth;
    private float thisBlockHeight;

    // Start is called before the first frame update
    void Start()
    {
        ball = GameObject.Find("ball");
        blockGenerator = GameObject.Find("blockGenerator");

        //FIXME:矩形の大きさを取得するには、RectTransformを使う必要があるが
        //アタッチして使おうとしてもなぜか使用することができないため
        //いい感じの値を打ち込んである。ちゃんとやるなら自動で取得する必要がある。
        ballWidth = ball.GetComponent<SpriteRenderer>().bounds.size.x;
        ballHeight = ball.GetComponent<SpriteRenderer>().bounds.size.y;
        thisBlockWidth = 0.78f;
        thisBlockHeight = 0.4f;
    }

    // Update is called once per frame
    void Update()
    {
        //FIXME:barクラスを見ると分かるが、かなり重複している
        //コリジョン専用のクラスを作っておいてそこから呼び出すようにしたほうがいいだろう
        Vector2 ballVector = ball.transform.position;
        Vector2 thisBlockVector = transform.position;
        bool checkFlag1 = ballVector.x <= thisBlockVector.x + thisBlockWidth;
        bool checkFlag2 = thisBlockVector.x <= ballVector.x + ballWidth;
        bool checkFlag3 = ballVector.y <= thisBlockVector.y + thisBlockHeight;
        bool checkFlag4 = thisBlockVector.y <= ballVector.y + ballHeight;


        if (checkFlag1 && checkFlag2 && checkFlag3 && checkFlag4)
        {
            
            ball.GetComponent<ball>().invertYVelocity();
            blockGenerator.GetComponent<blockGenerator>().incrementCountDestroyedBlock();
            Destroy(gameObject);
        }
    }


}
