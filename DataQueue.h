#pragma once
template<typename T>
/*
* DataQueue for data aquisition
* This queue is a FIFO templated queue to buffer data aquisition during collection
* Author: Taylor Coons
*/
class DataQueue
{
private:
	// DO NOT UNCOMMENT THESE!
	// PLEASE SEE Daiquiri DOCUMENTATION
	// CONFIG VARS
	// unsigned int queueSize = 10;

	// END CONFIG VARS
#include DataQueueConfig.h
public:
	DataQueue();

	/*
	* Enqueues a value into the queue.
	*/
	void enqueue(T value);

	/*
	* Returns the most recent value added to the queue.
	* This functions pulls the most recent value from the queue essentailly causing the queue to act as a stack (LIFO queue).
	*/
	T getRecentValue();

	/*
	* Returns the next value in the queue based on time.
	* This function pulls the next queued data entry, causing the queue to act as a standard queue (FIFO queue).
	*/
	T getNextValue();

	/*
	* Removes all data points except the most recent data point.
	* Deletes all data points except the one most recently entered into the queue. Queue size will gauranteed to be one.
	*/
	void squashQueueRecent();

	/*
	* Removes all data points except the next queued value based on time.
	* Deletes all elements in the queue except the oldest value based one time. Queue size will gauranteed to be one.
	*/
	void squashQueueNext();

	/*
	* Clears the queue causing the size to be zero
	*/
	void clearQueue();

	~DataQueue();
};

template<typename T>
DataQueue<T>::DataQueue() {
}

template<typename T>
void DataQueue<T>::enqueue(T value) {
}


template<typename T>
T DataQueue<T>::getRecentValue() {
}

template<typename T>
T DataQueue<T>::getNextValue() {
}

template<typename T>
void DataQueue<T>::squashQueueRecent() {
}

template<typename T>
void DataQueue<T>::squashQueueNext() {
}

template<typename T>
void DataQueue<T>::clearQueue() {
}

template<typename T>
DataQueue<T>::~DataQueue() {
}