![png](screenshots/Screenshot%202025-12-02%20233338.png)

![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fraw.githubusercontent.com%2Foffiicialkamal%2Fshare-storage%2Frefs%2Fheads%2Fmain%2Ftool.json&label=RUNS&countColor=%23263759)

![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Foffiicialkamal%2Fshare-storage%2F&countColor=%23263759)


## Desclaimer

This tool is designed for shairing files directly from your devices, very healpful to get your data from isolated invironments. the tool provides user friendly CLI Ui.

> [!CAUTION]
> The tool provides shairing files from your device / terminal so be carefull never share your link with anyone , user is responsible for his data so please use it carefully and observe logs/console to see what files are getting accessed.


## License & Partiality
The Project is released under <a href="https://github.com/offiicialkamal/share-storage/blob/main/LICENCE">"MIT Licence </a> and fully <a href="https://github.com/offiicialkamal/share-storage">Open-Source</a>

## Features

`Highly Portable` : The tool is able to upgrade itself according to your system does'nt matter which system you're using.

`auto installation` : the tool is able to detect the misssing modules and installs autometically according to the the respective system.

`Auto Update ` : The tool is Capable of checking and updating it self provides user friendly dashboard with multiple options

` Ui ` : Provides an impresive and Simple Ui even its an console based tool with auto.


## How To Use
You don't need to do anything manually just -

- select the option shown bellow according to your operatingg system or terminal
- then copy all respective **commands** ( avilable bellow ) at once.
- Paste all commands to your shell and hit enter
- possibly you'll asked to select between `Y/N` type `Y` each time and hit enter.

#### Commands
<details>
  <summary>Android ( Termux / Debain Linux )</summary>

  ```
  pkg update && pkg upgrade
  pkg install python -y
  pkg install git -y
  pkg install cloudflared -y
  git clone https://github.com/offiicialkamal/share-storage.git
  cd share-storage
  pip install -r requirements.txt
  ```
</details>


## Tech Stack

Tried to Avoide the thoird party modules and promots the use of standerd libraries but still we need external libraris so i used these external libraris

#### Third Party Libraries

the tool usage multiple third party libraries so such as -


|Libraries               |Purpose                                                                           |
|------------------------|----------------------------------------------------------------------------------|
| Requests               | To perform http requests and try to grab the informations such as Versions etc.. |
| cloudFlared            | To Expose localhost over the internet                                            |
| art                    | To Auto Generate the Respective Logo                                             |


#### Standerd Libraris

|Libraries               |Purpose                                                                         |
|------------------------|--------------------------------------------------------------------------------|
| os                     | for interacting operating system                                               |
| Subprocess             | for runnig multiple shell commands respective to the operating system          |
| WebBrowser             | for symplyfying the auto open respective websites                              |


## Support
- we are always hear to provide tool related support hear.
- Facing any kind of issues ? please open an new issue <a href="https://github.com/offiicialkamal/share-storage/issues"> Hear </a>

## Contributions
- In one word: **Welcome!**
- If you're a developer who wants to contribute or improve the project, remember: **“small steps make a big difference.”** I truly appreciate any kind of contribution you can offer

> [!INFO]
> I always appreciate a clear and proper description of the changes so I can understand the improvements and the impact of your contribution.






