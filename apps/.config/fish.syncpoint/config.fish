set EDITOR /bin/nano


function confirm
  while true
    read -l -P 'Do you want to continue? [y/N] ' resp

    switch $resp
      case Y y
        eval $argv
        return
      case '' N n
        return
    end
  end
end


alias private-home="mkdir $HOME/PRVTH; firejail --noprofile --private=$HOME/PRVTH fish"

alias logout="confirm qdbus org.kde.ksmserver /KSMServer logout 0 0 0"

alias hibernate="confirm systemctl hibernate"
