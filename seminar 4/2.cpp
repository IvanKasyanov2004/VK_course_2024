#include <iostream>
#include <vector>
using namespace std;


void ShellSort(vector<int> &arr){
    int n = arr.size();
    int gap = n / 2;
    while(gap > 0){
        for(int cur_pos = 0; cur_pos < n; cur_pos++){  //с одним гэпом двигаемся на 1 шаг вправо, пока не дойдем до конца
            int m_gap = cur_pos;
            while(m_gap >= gap and arr[m_gap] < arr[m_gap - gap]){  //последовательно сравниваем все элементы на расстоянии gap, меняем местами, если еще есть элемент слева и если левый юольше правого
                swap(arr[m_gap], arr[m_gap - gap]);
            }
        }
        gap = gap / 2;
    }
}

//накормить животных 
int feedAnimals(vector<int> &animals, vector<int> &food){
    if(animals.size() == 0 or food.size() == 0){
        return 0;
    }
    ShellSort(animals);  //сортируем еду и животных
    ShellSort(food);
    int count = 0;

    for(int i = 0; i < food.size(); i++){  //идем по еде
        if (food[i] >= animals[count]){  //проверяем, можно ли накормить кого-то
            count += 1;
        }
        if(count == animals.size()){ //если всех накормилои, а еда осталась, то дальше не идем
            break;
        }
    }
    return count;

}

int main(){
    vector<int> animals {8, 2, 3, 2};
    vector<int> food {1, 1, 3, 8};
    cout << feedAnimals(animals, food) << endl;
}