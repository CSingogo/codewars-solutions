{/**
Write a react component that will display the current value of our counter.

The counter should start at 0.
There should be a button to add 1.
There should also be a button to subtract 1.
We want to be able to see the value of the counter - so it should be rendered! And for your buttons to work they will need an onClick prop.

In your render you should return:

The counter display element with an id of 'counter', containing the counter value.
An increment button with an id of 'increment'
A decrement button with an id of 'decrement'
*/}

import React from 'react';

export class Counter extends React.Component {
  constructor(props) {
    super(props);
    this.state = {counter: 0}
  }
  
  // Your event handlers 
  add = () => {
    this.setState(prev => ({
      counter: prev.counter + 1
    }));
  }
  
  subtract = () => {
    this.setState(prev => ({
       counter: prev.counter - 1
    }));
  }
  
  render() {
    return (
      <div>
        <div id='counter'>
          {this.state.counter}
        </div>
          <button type="button" id='decrement' onClick={this.subtract}>
            Decrement
          </button>
          <button type="button" id='increment' onClick={this.add}>
            Increment
          </button>
      </div>
    )
  }
}