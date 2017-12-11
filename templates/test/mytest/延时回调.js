// 关于此函数我还是有着不理解之处的，就比如说，实例化CallBack之后，
// 为什么还能访问到i和arr呢  非常疑问
function CallBack() {
    var arr = [],
      i = 0;
    this.add = function (func) {
      arr.push(func);
    }

    this.run = function (num) {
      var fun = function () {
        if (i < arr.length) {
          arr[i++](fun)
        }
      }
      fun();
    }
  }

  var aa = new CallBack()

  aa.add(function (next) {
    console.log('0');
    next();
  })

  aa.add(function (next) {
    setTimeout(function () {
      console.log('1');
      next();
    }, 3000);
  })
  aa.add(function (next) {
    console.log('2');
    next();
  })
  aa.add(function (next) {
    setTimeout(function () {
      console.log('3');
      next();
    }, 1000);
  })

  console.log(new Date())
  aa.run()
  console.log(aa)