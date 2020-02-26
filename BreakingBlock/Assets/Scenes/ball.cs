using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;

public class ball : MonoBehaviour
{
    private const float CONFIGURED_BALL_SPEED = 0.08f;
    private float xBallVelocity = 0.0f;
    private float yBallVelocity = 0.0f;
    private float screenBottom;
    private float ballHeight;


    private Camera mainCamera;


    // Start is called before the first frame update
    void Start()
    {
        mainCamera = GameObject.Find("Main Camera").GetComponent<Camera>();
        ballHeight = GetComponent<SpriteRenderer>().bounds.size.y;
        screenBottom = getScreenBottom();
    }

    // Update is called once per frame
    void Update()
    {
        transform.Translate(xBallVelocity, yBallVelocity, 0);
        if(transform.position.y -  ballHeight <= -screenBottom)
        {
            SceneManager.LoadScene("GameOver");
        }
    }

    public void invertAllVelocity()
    {
        invertXVelocity();
        invertYVelocity();
    }

    public void invertXVelocity()
    {
        
        
        xBallVelocity = -xBallVelocity;
    }
    public void invertYVelocity()
    {
        yBallVelocity = -yBallVelocity;
    }

    private float getScreenBottom()
    {
        Vector3 bottomRight = mainCamera.ScreenToWorldPoint(new Vector3(Screen.width, Screen.height, 0.0f));
        return bottomRight.y;

    }

    public void moveBall()
    {
        xBallVelocity = -CONFIGURED_BALL_SPEED;
        yBallVelocity = -CONFIGURED_BALL_SPEED;
    }

}
