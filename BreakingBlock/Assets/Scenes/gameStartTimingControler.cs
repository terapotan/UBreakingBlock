using System.Collections;
using System.Collections.Generic;
using UnityEngine.UI;
using UnityEngine;

public class gameStartTimingControler : MonoBehaviour
{
    private GameObject ball;
    private GameObject startText;

    // Start is called before the first frame update
    void Start()
    {
        ball = GameObject.Find("ball");
        startText = GameObject.Find("startText");
    }

    // Update is called once per frame
    void Update()
    {
        if (Input.GetKeyDown(KeyCode.Space))
        {
            GameObject.Find("startPlayingMusic").GetComponent<startPlayingMusic>().startMusic();
            ball.GetComponent<ball>().moveBall();
            startText.GetComponent<Text>().enabled = false;
            Destroy(gameObject);
        }
    }
}
