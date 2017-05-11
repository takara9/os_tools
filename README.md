# os_tools
upload, download tools for SoftLayer Object Storage 

#SOFTLAYER Object Storage のupload / download サンプルツール

##python コード

- os_upload.py    ローカルPCからObject Storageへアップロード
- os_download.py  Object Storage からローカルPCヘダウンロード
- os_delete.py    Object Storageのオブジェクトを削除
- os_list.py      コンテナを指定してオブジェクトのリストを取得
- os_dump.py      dump コマンドと組み合わせて Linux のバックアップ
- os_restore.py　 restore コマンドと組み合わせて バックアップからのリストア

##認証情報サンプル
- credentials.json.sample このファイルの.sample を削除してjsonファイルとして利用します。
　　　 このファイルに、オブジェクト・ストレージのユーザーIDとパスワードをセットします。
  
##機能

オブジェクト・ストレージには、5Gバイトを超えるサイズのファイルを登録できないという制約があります。この制約を補完する機能はオブジェクト・ストレージに備わっているのですが、APIを利用しないと利用できない課題がありました。このサンプルは、5GBを超えるファイルの登録と取得を一括でおこなうものです。

このツールでは、マニフェストというオブジェクトを作成して、大きなファイルをチャックに分けて登録します。カスタマーポータル上は、一個のオブジェクトしか見えず、この一個をクリックすると、5GBを超える大きなオブジェクトを取得する事が出来ます。　カスタマーポータルでラージ・オブジェクトを操作するのは大変です。また、CloudBerryを使ったり、Swiftコマンドをインストールするのも面倒という場合に役立つツールです。


##インストール方法


SoftLayerの仮想サーバーとパソコンにインストールして利用のどちらでも、対応できます。


### CentOS6 x86_64 の場合

CentOS6では、InsecurePlatformWarningのワーニングが表示されるので、pip install requests==2.5.3 を実行してバージョンを下げることで対応します。

    yum update -y
    python --version
    Python 2.6.6
    rpm -ivh http://dl.fedoraproject.org/pub/epel/6/x86_64/epel-release-6-8.noarch.rpm
    yum install -y git
    yum install -y python-pip
    pip install softlayer-object-storage
    pip install requests==2.5.3
    git clone https://github.com/takara9/os_tools.git
    cd os_tools
    ls
    README.md os_delete.py	os_download.py	os_list.py	os_upload.py

この後、それぞれのファイルのusername,api-keyを変更して実行します。
CentOS7 x86_64の場合は、rpm -iUvh http://dl.fedoraproject.org/pub/epel/7/x86_64/e/epel-release-7-5.noarch.rpm  に置き換えます。


### Ubuntu 14.04 x86_64 の場合

    apt-get update
    apt-get upgrade -y
    python --version
    Python 2.7.6
    apt-get install python-pip -y
    pip install softlayer-object-storage
    apt-get install git -y
    git clone https://github.com/takara9/os_tools.git
    cd os_tools
    ls
    README.md os_delete.py	os_download.py	os_list.py	os_upload.py

この後、それぞれのファイルのusername,api-keyを変更して実行します。


### MacOS 10.9 の場合

最初からPythonが入っているので、pipのインストールから始めます。

    sudo -s
    easy_install pip
    pip install softlayer-object-storage
    pip install requests==2.5.3
    exit
    git clone https://github.com/takara9/os_tools.git
    cd os_tools
    ls
    README.md os_delete.py	os_download.py	os_list.py	os_upload.py

この後は同じです。 Ubuntuの場合と同じです。


### Windows 8.1 / Windows 7 の場合

最初にPythonとsetuptoolsをインストールします。 Pythonのインストールは、https://www.python.org/downloads/windows/  から2.7系の最新版をダウンロードして導入します。 環境変数のPathにC:\Python27;C:\Python27\Scriptsを加えます。

次にWindows PowerShellを起動してsetuptoolsを次のコマンドを実行します。詳しい解説は、https://pypi.python.org/pypi/setuptools  のページにあります。

    (Invoke-WebRequest https://bootstrap.pypa.io/ez_setup.py).Content | python -
    exit

次に、pipなど必要なソフトウェアを導入していきます。

    easy_install pip
    pip install softlayer-object-storage
    pip install requests==2.5.3

Windowsのgitは、https://msysgit.github.io/  からダウンロードしてインストールします。環境変数のPathにgitの導入先のC:\Program Files (x86)\Git\binを追加します。コマンド プロンプトを起動してクローンを作成します。

    git clone https://github.com/takara9/os_tools.git
    cd os_tools
    ls
    README.md os_delete.py	os_download.py	os_list.py	os_upload.py

この後は他のOSと同じです。



### usernameとapi-keyの取得方法

オブジェクト・ストレージを利用するには、SOFTLAYERのポータル画面のAccount -> Usersで得られるユーザー名とAPIキーではなく、オブジェクト・ストレージのユーザー名とキーが必要です。

オブジェクト・ストレージのユーザー名とAPIキーの取得は、以下の順になります。
Storage -> Object Storage -> [Object Storage User Id] -> [Datacenter] -> View Credentials

オブジェクト・ストレージのユーザー名を取得していない場合は、Storage -> Object Storage -> Order Object Storage からオーダーして、ユーザー名を取得できます。


##使い方

それぞれのPythonコードに、引数の個数が正しく無い場合のメッセージを付けていますので、コードを見るのが、一番安心できると思います。

					
##使用例

最初に、Pythonコードの先頭部分にある以下の３項目を利用環境に合わせて変更します。

    ###
    # ユーザーID、パスワード、データセンター（ラベル）
    uid = 'SL123456-1:SL123456'
    upw = '71a8c0f9cd9*****************************************************'
    odc = 'tok02'


###(a) アップロード
   
引数は３個で、それぞれ以下の様になります。ローカルファイルをチャンク・サイズに分割して転送しますから、5Gバイトの制限を超えるファイルサイズでもアップロードできます。ダウロードの際は、このオブジェクト名は、マニフェストになっているので、チャンクに分割されたオブジェクトを１本のファイルに統合してダウンロードできます。
  
    $ os_upload.py ローカルファイル名 コンテナ名 オブジェクト名

コマンドの使用例で、サイズを表示後、チャンク・サイズ毎に、順次アップロードします。

    $ ./os_upload.py test17-2.vhd VHD test17.vhd-0.vhd
    input file size = 4354803712
    sending...  0.0 %
    sending...  4.8 %
    sending...  9.6 %
    <-- 省略 -->
    sending...  91.5 %
    sending...  96.3 %


###(b) ダウンロード

コマンドの引数は、３個で以下になります。

    $ ./os_download.py コンテナ名 オブジェクト名 保存先ファイル名

利用例です。実行中は異常終了しない限り、メッセージも何も表示しません。

    $ ./os_download.py VHD test8.vhd-0.vhd testimage.vhd
    $


###(c) コンテナ内のオブジェクトのリスト取得

引数はコンテナ名だけです。次の実行例では、コンテナ iso に含まれるオブジェクトのリストを表示しています。 これは前述のアップロードツールを利用して登録したものですが、カスタマー・ポータル画面上では、マニフェストである ubuntu-14.04.2-server-amd64.iso のみ表示される事になります。実態のチャンクを参照するために、このツールを利用することができます。

    $ ./os_list.py iso
    StorageObject(iso, ubuntu-14.04.2-server-amd64.iso/chunk-0002/path, UnknownB)
    StorageObject(iso, ubuntu-14.04.2-server-amd64.iso/chunk-0003/path, UnknownB)
    StorageObject(iso, ubuntu-14.04.2-server-amd64.iso/path, UnknownB)
    StorageObject(iso, ubuntu-14.04.2-server-amd64.iso/chunk-0001/path, UnknownB)


###(d) 削除

オブジェクトを一つ一つ削除するのは大変なので、マニフェスト名を指定して、その実態のチャンクも含めて削除するコマンドです。

    $ ./os_delete.py iso ubuntu-14.04.2-server-amd64.iso
    Delete StorageObject(iso, ubuntu-14.04.2-server-amd64.iso/chunk-0002, 0B)
    Delete StorageObject(iso, ubuntu-14.04.2-server-amd64.iso/chunk-0001, 0B)
    Delete StorageObject(iso, ubuntu-14.04.2-server-amd64.iso/chunk-0003, 0B)
    $ ./os_list.py iso
    $



##関連参照先
- SoftLayer Object Storage Python Client https://github.com/softlayer/softlayer-object-storage-python

##作成者  

高良 真穂 (Maho Takara)
takara@jp.ibm.com, takara9@gmail.com, @MahoTakara
https://www.facebook.com/profile.php?id=100002198440895


##日付

2015/6/4
