# PEAS
Original PEAS (https://github.com/WithSecureLabs/peas) is a Python 2 library and command line application for running commands on an ActiveSync server e.g. Microsoft Exchange. It is based on [research](https://labs.mwrinfosecurity.com/blog/accessing-internal-fileshares-through-exchange-activesync) into Exchange ActiveSync protocol by Adam Rutherford and David Chismon of MWR.

## Optional installation
`python setup.py install`

# PEAS application
PEAS can be run without installation from the parent `peas` directory (containing this readme). PEAS can also be run with the command `peas` after installation.

## Running PEAS

`python3 -m peas [options] <server>`


## Example usage
### Check server
`python3 -m peas 10.207.7.100`

### Check credentials
`python3 -m peas --check -u luke2 -p ChangeMe123 10.207.7.100`

### Get emails
`python3 -m peas --emails -u luke2 -p ChangeMe123 10.207.7.100`

### Save emails to directory
`python3 -m peas --emails -O emails -u luke2 -p ChangeMe123 10.207.7.100`

### List file shares
`python3 -m peas --list-unc='\\fictitious-dc' -u luke2 -p ChangeMe123 10.207.7.100`

`python3 -m peas --list-unc='\\fictitious-dc\guestshare' -u luke2 -p ChangeMe123 10.207.7.100`

**Note:** Using an IP address or FQDN instead of a hostname in the UNC path may fail.

### View file on file share
`python3 -m peas --dl-unc='\\fictitious-dc\guestshare\fileonguestshare.txt' -u luke2 -p ChangeMe123 10.207.7.100`

### Save file from file share
`python3 -m peas --dl-unc='\\fictitious-dc\guestshare\fileonguestshare.txt' -o file.txt -u luke2 -p ChangeMe123 10.207.7.100`

### Command line arguments

Run `python3 -m peas --help` for the latest options.

    Options:
      -h, --help            show this help message and exit
      -u USER               username
      -p PASSWORD           password
      --smb-user=USER       username to use for SMB operations
      --smb-pass=PASSWORD   password to use for SMB operations
      --verify-ssl          verify SSL certificates (important)
      -o FILENAME           output to file
      -O PATH               output directory (for specific commands only, not
                            combined with -o)
      -F repr,hex,b64,stdout,stderr,file
                            output formatting and encoding options
      --check               check if account can be accessed with given password
      --emails              retrieve emails
      --list-unc=UNC_PATH   list the files at a given UNC path
      --dl-unc=UNC_PATH     download the file at a given UNC path

 
## Limitations 
 
PEAS has been tested on Kali 2.0 against Microsoft Exchange Server 2013 and 2016. The domain controller was Windows 2012 and the Exchange server was running on the same machine. Results with other configurations may vary.

py-eas-client support is limited to retrieving emails and causes a dependency on Twisted. It was included when the library was being evaluated but it makes sense to remove it from PEAS now, as all functionality can be provided by pyActiveSync.

The licence may be restrictive due to the inclusion of pyActiveSync, which uses the GPLv2.

The requirement to know the hostname of the target machine for file share access may impede enumeration.
