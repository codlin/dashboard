export const getTimestamp = () => {
  return new Date().getTime()
}

export const getBeforeDate = n => {
  var date = new Date()
  var year, month, day
  date.setDate(date.getDate() - n)
  year = date.getFullYear()
  month = date.getMonth() + 1
  day = date.getDate()

  let s =
    year +
    '-' +
    (month < 10 ? '0' + month : month) +
    '-' +
    (day < 10 ? '0' + day : day)

  return s
}

// +---------------------------------------------------
// | get current date format: YYYY-MM-dd
// +---------------------------------------------------
export const getCurrentDate = () => {
  var date = new Date()
  var year = date.getFullYear()
  var month = date.getMonth() + 1
  var day = date.getDate()
  if (month < 10) {
    month = '0' + month
  }
  if (day < 10) {
    day = '0' + day
  }
  var nowDate = year + '-' + month + '-' + day
  return nowDate
}

// +---------------------------------------------------
// | date format: YYYY-MM-dd HH:MM:SS
// +---------------------------------------------------
export const getDuration = (startTime, endTime) => {
  // convert time format xxxx-xx-xx to xxxx/xx/xx
  startTime = startTime.replace(/-/g, '/')
  endTime = endTime.replace(/-/g, '/')

  var start = new Date(startTime)
  var end = new Date(endTime)
  let duration = end.getTime() - start.getTime() // seconds

  var days = Math.floor(duration / (24 * 3600 * 1000))
  var leave1 = duration % (24 * 3600 * 1000) // 计算天数后剩余的毫秒数
  var hours = Math.floor(leave1 / (3600 * 1000)) // 计算相差小时数
  var leave2 = leave1 % (3600 * 1000) // 计算小时数后剩余的毫秒数
  var minutes = Math.floor(leave2 / (60 * 1000)) // 计算相差分钟数
  var leave3 = leave2 % (60 * 1000) // 计算分钟数后剩余的毫秒数
  var seconds = Math.round(leave3 / 1000) // 计算分钟数后剩余的秒数
  return [days, hours, minutes, seconds]
}

// +---------------------------------------------------
// | compute days between tow dates format: 'YYYY-MM-dd'
// +---------------------------------------------------
export const daysBetween = (DateOne, DateTwo) => {
  var OneMonth = DateOne.substring(5, DateOne.lastIndexOf('-'))
  var OneDay = DateOne.substring(DateOne.length, DateOne.lastIndexOf('-') + 1)
  var OneYear = DateOne.substring(0, DateOne.indexOf('-'))

  var TwoMonth = DateTwo.substring(5, DateTwo.lastIndexOf('-'))
  var TwoDay = DateTwo.substring(DateTwo.length, DateTwo.lastIndexOf('-') + 1)
  var TwoYear = DateTwo.substring(0, DateTwo.indexOf('-'))

  var cha =
    (Date.parse(OneMonth + '/' + OneDay + '/' + OneYear) -
      Date.parse(TwoMonth + '/' + TwoDay + '/' + TwoYear)) /
    86400000
  return Math.abs(cha)
}

export const isObjectValueEqual = (x, y) => {
  // If both x and y are null or undefined and exactly the same
  if (x === y) {
    return true
  }

  // If they are not strictly equal, they both need to be Objects
  if (!(x instanceof Object) || !(y instanceof Object)) {
    return false
  }

  // They must have the exact same prototype chain, the closest we can do is
  // test the constructor.
  if (x.constructor !== y.constructor) {
    return false
  }

  for (var p in x) {
    // Inherited properties were tested using x.constructor === y.constructor
    if (x.hasOwnProperty(p)) {
      // Allows comparing x[ p ] and y[ p ] when set to undefined
      if (!y.hasOwnProperty(p)) {
        return false
      }

      // If they have the same strict value or identity then they are equal
      if (x[p] === y[p]) {
        continue
      }

      // Numbers, Strings, Functions, Booleans must be strictly equal
      if (typeof x[p] !== 'object') {
        return false
      }

      // Objects and Arrays must be tested recursively
      if (!Object.equals(x[p], y[p])) {
        return false
      }
    }
  }

  for (p in y) {
    // allows x[ p ] to be set to undefined
    if (y.hasOwnProperty(p) && !x.hasOwnProperty(p)) {
      return false
    }
  }
  return true
}
