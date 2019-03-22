// **************************
// FOR LOOP
// **************************
// Runs to termination
// No ability to reset
// Looping, not iterating
for (let i = 0; i < 6; i++) {
  console.log(i) // outputs 0 - 5 right away
}

// **************************
// GENERATOR
// **************************
// Runs as its called
// Can be reset through re-instantiation (with custom values)
// Will instantiate a Generator, which is an iterator - inherently stateful
function * generateX(max) {
  console.log('running generator')
  let idx = 0
  while(idx < max) {
    yield idx
    idx++
  }
}

// Create generator
const logger = generateX(6)

// Go crazy with logs
console.log(logger.next().value) // logs 0
console.log('Waiting for next value')
console.log(logger.next().value) // logs 1 - stateful!
setTimeout(() => {
  console.log('Now logging async values')
  console.log(logger.next().value)
  console.log(logger.next().value)
}, 3000) // log '2' and '3' after 3 seconds
console.log('this is past the setTimeout')
console.log(logger.next().value)
console.log(logger.next().value)

// **************************
// SCHEDULER - NO GENERATOR
// **************************

// const pieces = ['scales', 'Hanon', 'Minuet in G', 'King March']
//
// const numWeeks = 3
// const daysPerWeek = 6
//
// const totalPracticeDays= numWeeks * daysPerWeek;
//
// let currentMusicIndex = 0
//
// const schedule = [...Array(totalPracticeDays)].map(() => ({
//     practice: pieces[currentMusicIndex++ % pieces.length]
// }))
//
// console.log(schedule)


// **************************
// SCHEDULER - WITH GENERATOR
// **************************

// function * repeater(arr) {
//   let index = 0
//   while (true) {
//     yield arr[index++ % arr.length]
//   }
// }
//
// const pieces = ['scales', 'Hanon', 'Minuet in G', 'King March']
// const numWeeks = 3
// const daysPerWeek = 6
// const totalSessions = numWeeks * daysPerWeek
// const nextPiece = repeater(practicePieces)
//
// const schedule = [...Array(totalSessions)].map(() => ({
//   practice: nextPiece.next().value
// }))
//
// console.log(schedule

// **************************
// FIBONACCI GENERATOR
// **************************

function * fib() {
  // YOUR CODE HERE
}

// Create Fibonacci generator
const fibGenerator = fib()

// Logs the first 10 Fibonacci numbers
let index = 0
while ( index < 10) {
  console.log(fibGenerator.next().value)
  index++
}
