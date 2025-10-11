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

    int64_t n;
    cin >> n;

    int64_t capacity;
    cin >> capacity;

    int64_t summ = 0;
    for (int i = 0; i < n; i++) {
        string action;
        cin >> action;

        if (action == "print") {
            cout << summ << endl;
        } else {
            int64_t to_insert;
            cin >> to_insert;

            mh.insert(to_insert);
            summ += to_insert;
            
            if (mh.size() > capacity) {
                summ -= mh.extractMin();
            }
        }
    }

    return 0;
}
