#include <iostream>
#include <math.h>
using namespace std;
int main()
{
	srand((unsigned int)time(0));
	// number baseball
	int iBSNum[9] = {};
	for (int i = 0; i < 9; ++i)
	{
		iBSNum[i] = i + 1;
	}
	int iTemp, idx1, idx2;
	for (int i = 0; i < 100; i++)
	{
		idx1 = rand() % 9;
		idx2 = rand() % 9;

		iTemp = iBSNum[idx1];
		iBSNum[idx1] = iBSNum[idx2];
		iBSNum[idx2] = iTemp;
	}
	cout << "맞춰야 할 숫자" << endl;
	for (int i = 0; i < 3; i++)
	{
		cout << iBSNum[i];
	}
	cout << endl;
	int iMynum;
	int iMynum1;
	int iMynum2;
	int iMynum3;
	int iBall;
	int iStrike;
	while (true)
	{	
		while (true)
		{
			cout << "숫자를 입력하세요. : ";
			cin >> iMynum;
			iMynum1 = iMynum / 100;
			iMynum2 = iMynum % 100 / 10;
			iMynum3 = iMynum % 10;
			if ((iMynum <1000 && iMynum >= 100 && iMynum1 != iMynum2 && iMynum1 != iMynum3 && iMynum2 != iMynum3)||iMynum == 0)
			{
				break;
			}
		}
		if (iMynum == 0)
		{
			break;
		}
		iBall = 0;
		iStrike = 0;
		
		if (iMynum1 == iBSNum[0])
		{
			iStrike += 1;
		}
		else if(iMynum1 == iBSNum[1] || iMynum1 == iBSNum[2])
		{
			iBall += 1;
		}

		if (iMynum2 == iBSNum[1])
		{
			iStrike += 1;
		}
		else if (iMynum2 == iBSNum[0] || iMynum2 == iBSNum[2])
		{
			iBall += 1;
		}

		if (iMynum3 == iBSNum[2])
		{
			iStrike += 1;
		}
		else if (iMynum3 == iBSNum[0] || iMynum3 == iBSNum[1])
		{
			iBall += 1;
		}

		cout << "Strike : " << iStrike << " Ball : " << iBall << endl;
		if (iStrike == 3)
		{
			cout << "게임종료" << endl;
			break;
		}
		else
		{
			cout << "다시 입력 하세요" << endl;
		}
	}
	return 0;
}