using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class startPlayingMusic : MonoBehaviour
{
    public void startMusic()
    {
        GetComponent<AudioSource>().Play();
    }
}
