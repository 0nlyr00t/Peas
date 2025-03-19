__author__ = 'Adam Rutherford'

from twisted.internet import reactor

from .eas_client import activesync


def body_result(result, emails, num_emails):

    emails.append(result['Properties']['Body'])

    # Stop after receiving final email.
    if len(emails) == num_emails:
        reactor.stop()


def sync_result(result, fid, async_flag, emails):

    assert hasattr(result, 'keys')

    num_emails = len(list(result.keys()))

    for fetch_id in list(result.keys()):

        async_flag.add_operation(async_flag.fetch, collectionId=fid, serverId=fetch_id,
            fetchType=4, mimeSupport=2).addBoth(body_result, emails, num_emails)


def fsync_result(result, async_flag, emails):

    for (fid, finfo) in result.items():
        if finfo['DisplayName'] == 'Inbox':
            async_flag.add_operation(async_flag.sync, fid).addBoth(sync_result, fid, async_flag, emails)
            break


def prov_result(success, async_flag, emails):

    if success:
        async_flag.add_operation(async_flag.folder_sync).addBoth(fsync_result, async_flag, emails)
    else:
        reactor.stop()


def extract_emails(creds):

    emails = []

    async_flag = eas_client.activesync.ActiveSync(creds['domain'], creds['user'], creds['password'],
            creds['server'], True, device_id=creds['device_id'], verbose=False)

    async_flag.add_operation(async_flag.provision).addBoth(prov_result, async_flag, emails)

    reactor.run()

    return emails
