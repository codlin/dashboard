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
