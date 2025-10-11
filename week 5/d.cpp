#include <iostream>
#include <vector>
using namespace std;

class MinHeap {
private:
    vector<int64_t> heap;  // храним кучу в векторе

    // Просеивание вверх (когда вставляем новый элемент)
    void heapifyUp(int index) {
        while (index > 0) {
            int parent = (index - 1) / 2;
            if (heap[parent] > heap[index]) {
                swap(heap[parent], heap[index]);
                index = parent;
            } else break;
        }
    }

    // Просеивание вниз (когда удаляем минимум и ставим последний элемент наверх)
    void heapifyDown(int index) {
        int size = heap.size();
        while (true) {
            int left = 2 * index + 1;
            int right = 2 * index + 2;
            int smallest = index;

            if (left < size && heap[left] < heap[smallest])
                smallest = left;
            if (right < size && heap[right] < heap[smallest])
                smallest = right;

            if (smallest != index) {
                swap(heap[index], heap[smallest]);
                index = smallest;
            } else break;
        }
    }

public:
    // Вставка нового элемента
    void insert(int64_t value) {
        heap.push_back(value);
        heapifyUp(heap.size() - 1);
    }

    // Забрать минимальный элемент (корень)
    int64_t extractMin() {
        if (heap.empty()) {
            throw runtime_error("Heap is empty");
        }
        int64_t minValue = heap[0];
        heap[0] = heap.back();  // переносим последний элемент наверх
        heap.pop_back();
        if (!heap.empty())
            heapifyDown(0);
        return minValue;
    }

    // Посмотреть минимум
    int getMin() const {
        if (heap.empty()) throw runtime_error("Heap is empty");
        return heap[0];
    }

    bool empty() const {
        return heap.empty();
    }

    int size() const {
        return heap.size();
    }
};

int main() {
    MinHeap mh;

    int n;
    cin >> n;

    int m;
    cin >> m;

    for (int i = 0; i < n; i++) {
        int64_t to_insert;
        cin >> to_insert;
        mh.insert(to_insert);
    }

    int cnt = 0;
    int64_t least;
    int64_t sec_least;
    while (mh.getMin() < m) {
        if (mh.size() == 1) {
            cout << -1;
            return 0;
        }

        cnt++;
        
        least = mh.extractMin();
        sec_least = mh.extractMin();

        mh.insert(least + 2 * sec_least);
    }

    cout << cnt << endl;

    return 0;
}
