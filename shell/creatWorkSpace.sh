DEBUG()
{
  if [ "$DEBUG" = "true" ]; then
    $@..
  fi
}

function creatWs()
{

    tryTimes="1 2 3"
    
    #---------------------creat folder at root directory-----------------#
    while [ "$PWD" != "/home/b2li" ]
    do
        cd ..
    done

    for loop in $tryTimes
    do
        echo "please input the work space name"
        read wsName
        echo "work space name: $wsName"
        if [ -d "$wsName" ]; then
            echo "the work  space has exist!!!"
        elif [ "$wsName" = "" ]; then
            echo "the work space name can't be empty!!!"
        else
            break
        fi

        if [ "$loop" = "3" ]; then
            exit 1
        fi

    done

    mkdir ~/$wsName 
    cd ~/$wsName

    # ---------------------download script--------------------------#
    for loop in $tryTimes
    do
        echo -e "select rlease version: 1.RL45 2. RL55 (RL55 is default)"
        read releaseVersion
        
        svnPathBase="https://beisop60.china.nsn-net.net/isource/svnroot/BTS_SC_UL_PHY_TDD/A_TDLTE"
        if  [ "$releaseVersion" = "" ] || [ "$releaseVersion" = "RL55" ] || [ "$releaseVersion" = "2" ]; then
            svnPathRL55=$svnPathBase"/trunk/E_External/BuildScripts"
            svn co "$svnPathRL55" tscript
            break
        elif [ "$releaseVersion" = "RL45" ] || [ "$releaseVersion" = "1" ]; then
            svnPathRL45=$svnPath"/branches/branch_RL45/E_External/BuildScripts"
            svn co "$svnPathRL45" tscript
            break
        else
            echo "unknow release version: $releaseVersion"
        fi

        if [ "$loop" = "3" ]; then
            exit 2 
        fi

    done

    #-------------------------change script property-------------------------#
    cp tscript/* .
    rm -rf tscript
    chmod 777 *.sh
    dos2unix *.sh

    #------------------------download code-----------------------------#
    if [ -f "create_workspace.sh" ]; then
        ./create_workspace.sh -h
    else
        echo "no file 'create_workspace.sh'!!! "
        exit 4
    fi

    for loop in $tryTimes
    do
        echo "select : 1: local 2: ci (local is default)"
        read Local_or_CI
        if [ "$Local_or_CI" = "" ] || [ "$Local_or_CI" = "1" ] || [ "$Local_or_CI" = "local" ]; then
            Local_or_CI="local"
            break
        elif [ "$Local_or_CI" = "2" ] || [ "$Local_or_CI" = "ci" ]; then
            Local_or_CI="ci"
            break
        elif [ "$loop" -le "3" ]; then
            echo "unknow selction, please input again : 1: local 2: ci (local is default)"
        else
            exit 5
        fi
    done

    for loop in $tryTimes
    do
        echo "select : 1: without_sack 2: with_sack (without_sack is default)"
        read sack_or_not
        if [ "$sack_or_not" = "" ] || [ "$sack_or_not" = "1" ] || [ "$sack_or_not" = "without_sack" ]; then
            sack_or_not="without_sack"
            break
        elif [ "$sack_or_not" = "2" ] || [ "$sack_or_not" = "without_sack" ]; then
            sack_or_not="with_sack"
            break
        elif [ "$loop" -le "3" ]; then
            echo "unknow selction, please input again : 1: without_sack 2: with_sack (without_sack is default)"
        else
            exit 6
        fi
    done

    # ./create_workspace.sh $Local_or_CI $sack_or_not
    ./create_workspace.sh

    ./make.sh

}


#------------------------test code-------------------------#
function main()
{
    tryTimes="1 2 3"
    for loop in $tryTimes
    do
        echo $loop
    done

    #/home/b2li/myScript/setPath.sh
    setPath.sh
    creatWs
}

main


