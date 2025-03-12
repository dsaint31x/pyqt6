# Terminal

> Commnad Line Interface (CLI, or Character User Interface)에서 사용자가 컴퓨터에게 command를 입력하고 컴퓨터로부터 응답을 text로 받는 hardware device나 software를 가르킴.

Terminal은 우리나라 말로 하면 단말기 이지만, 터미널이라고 부르는 게 보다 일반적이다. 단말기의 경우 hardware적인 느낌이 강한데 현재의 terminal들은 거의 software인 경우가 대부분이기 때문이다.

## 유래

1960년대에 컴퓨터와 상호작용을 하던 방법은 `teletype` (전신타자기)를 이용하는 형태로 일종의 타자기 처럼 생긴 단말(terminal)에서 컴퓨터에게 command를 입력하면 출력이 종이로 인쇄되어 나오는 방식이었다.

![Teletype Model 33](https://en.wikipedia.org/wiki/Teletype_Model_33#/media/File:Teletype-IMG_7287.jpg)

> 종이로 출력이 되는 형태를 hard-copy terminal이라고도 부름.

이들 `teletype`를 `terminal`이라고 지칭하던 것에서 오늘날에도 CLI를 제공해주는 SW나 Hardware를 `terminal`이라고 부른다. (Console이라고도 불림.)

<iframe width="560" height="315" src="https://www.youtube.com/embed/S81GyMKH7zw?start=268" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

## 현대의 Terminal

모든 OS가 CLI를 위해서 `terminal`을 제공하고 있는데, 이들은 유래에서 살펴보았듯이 CLI를 위한 물리적 단말기를 Software로 구현한 일종의 terminal emulator로서 terminal을 통해 사용자가 command를 입력하면 이를 명령어 해석하는 프로그램(linux의 Shell)이 해석하여 OS에게 해당 작업을 수행시키고 이를 수행하면 다시 shell이 적절할 text로 terminal에 출력하게 된다. 때문에 엄밀하게 애기하면 `terminal emulator` 혹은 `virtual terminal`이라고 해야하지만, 줄여서 부르는 게 대세인 이쪽 세계에서 이런 호칭은 시험지 답안지 쓸 때나 사용되는게 현실이다. 

> 모니터를 출력으로 하는 Terminal emulator 관련하여 ANSI X3.64 의 일부 부분에서 표준이 존재함.

`teletype`에서 따온 약자인 `tty`는 linux나 macOS에서 터미널을 의미하는 약어로 많이 사용되며, `terminal`에 `tty`라고 입력할 경우, 현재 OS와 shell을 통해 연결되어 있는 `terminal` 의 식별자(정확히는 `stdin`과 연결된 terminal의 file name : linux에선 모든 디바이스를 file처럼 다룸.)를 반환해준다.

LinuxMint 21.1 (vera)에서 이를 수행하면 다음과 같이 나온다.

```Bash
(base) dsaint31@dsaint31-All-Series:~$ tty
/dev/pts/2
```

Windows에서는 `cmd` 가 바로 terminal을 수행하는 명령어 이지만, 최근엔 Window Subsystem Linux의 등장으로 cmd보다 `wsl ~` 또는 `bash`를 더 많이 애용되는 것으로 보인다 (CLI쓰는 사용자들의 특성상 어쩔 수 없는 추세인 듯). 또한 serial connection장비나 ssh연결 등에 사용되는 `putty`도 windows에서 애용되는 terminal이다.

ms store에 가면, 기존의 `cmd`보다 훨씬 좋은 interface의 `terminal` application을 제공한다 (이름이 `Windows Terminal`이고 테마 설정하면 꽤 쓸만하다). 웹브라우저 처럼 생긴 `MobaXTerm`도 꽤 많이 사용된다 (유로이나 무료로도 왠만한 기능은 사용가능함). 

Linux의 경우, 그냥 terminal 위주라.. ==;;. macOS도 BSD를 기반으로 했기 때문에 역시 terminal을 제공한다.



