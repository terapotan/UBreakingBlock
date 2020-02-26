using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;


public class blockGenerator : MonoBehaviour
{
    public GameObject blockPrefab;
    private int generatedBlockCount;
    private int destroyedBlockCount = 0;

    // Start is called before the first frame update
    void Start()
    {
        float startX = -5.0f;
        float startY = 1.9f;

        int rowValue = Random.Range(2, 5);
        int colValue = Random.Range(8, 15);

        generatedBlockCount = rowValue * colValue;

        for(int row = 0; row < rowValue; row++)
        {
            for(int col = 0;col < colValue; col++)
            {
                GameObject tmp = Instantiate(blockPrefab) as GameObject;
                tmp.transform.position = new Vector3(startX + 0.95f * col, startY + 0.8f * row , 0);

            }
        }
    }

    // Update is called once per frame
    void Update()
    {
        
    }

    public void incrementCountDestroyedBlock()
    {
        GetComponent<AudioSource>().Play();
        destroyedBlockCount++;

        if(destroyedBlockCount >= generatedBlockCount)
        {
            SceneManager.LoadScene("GameClear");
        }
    }
}
