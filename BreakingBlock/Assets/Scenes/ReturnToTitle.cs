﻿using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;


public class ReturnToTitle : MonoBehaviour
{
    public void ButtonClick()
    {
        SceneManager.LoadScene("GameTitle");
    }
}
