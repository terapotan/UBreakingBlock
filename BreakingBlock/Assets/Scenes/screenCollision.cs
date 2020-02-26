using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class screenCollision : MonoBehaviour
{
    private Camera mainCamera;
    private GameObject ball;

    private float screenLeftCoordinate;
    private float screenRightCoordinate;
    private float screenTopCoordinate;
    private float screenBottomCoordinate;

    private float ballWidth;
    private float ballHeight;

    // Start is called before the first frame update
    void Start()
    {
        mainCamera = GameObject.Find("Main Camera").GetComponent<Camera>();
        ball = GameObject.Find("ball");

        screenLeftCoordinate = getScreenLeft();
        screenRightCoordinate = getScreenRight();
        screenTopCoordinate = getScreenTop();
        screenBottomCoordinate = getScreenBottom();

        ballWidth = ball.GetComponent<SpriteRenderer>().bounds.size.x;
        ballHeight = ball.GetComponent<SpriteRenderer>().bounds.size.y;
    }

    // Update is called once per frame
    void Update()
    {
        if ((ball.transform.position.x - ballWidth)< screenLeftCoordinate)
        {
            ball.GetComponent<ball>().invertXVelocity();
        }

        if((ball.transform.position.x + ballWidth)> screenRightCoordinate)
        {
            ball.GetComponent<ball>().invertXVelocity();
        }

        if ((ball.transform.position.y - ballHeight) < screenTopCoordinate)
        {
            ball.GetComponent<ball>().invertYVelocity();
        }

        if ((ball.transform.position.y + ballHeight) > screenBottomCoordinate)
        {
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

    private float getScreenTop()
    {
        Vector3 topLeft = mainCamera.ScreenToWorldPoint(Vector3.zero);
        return topLeft.y;
    }

    private float getScreenBottom()
    {
        Vector3 bottomRight = mainCamera.ScreenToWorldPoint(new Vector3(Screen.width, Screen.height, 0.0f));
        return bottomRight.y;

    }
}
