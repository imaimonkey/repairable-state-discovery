# V2R cluster inventory

2026-09-24T08:59:44.761724+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 324377210880 available bytes; 81.90% used; 112490156 free inodes.

server1 `/home`: 324377210880 available bytes; 81.90% used; 112490156 free inodes.

server1 `/tmp`: 324377210880 available bytes; 81.90% used; 112490156 free inodes.

server1 `/var/tmp`: 324377210880 available bytes; 81.90% used; 112490156 free inodes.

server1 `/mnt/raid5`: 503749746688 available bytes; 97.69% used; 337716985 free inodes.
| server2 | True | [] | [] |

server2 `/`: 57788862464 available bytes; 96.78% used; 110430975 free inodes.

server2 `/home`: 57788862464 available bytes; 96.78% used; 110430975 free inodes.

server2 `/tmp`: 57788862464 available bytes; 96.78% used; 110430975 free inodes.

server2 `/var/tmp`: 57788862464 available bytes; 96.78% used; 110430975 free inodes.

server2 `/mnt/raid5`: 494917783552 available bytes; 96.58% used; 445178587 free inodes.
| server3 | True | ['0'] | [] |

server3 `/`: 85898981376 available bytes; 95.21% used; 114199583 free inodes.

server3 `/home`: 85898981376 available bytes; 95.21% used; 114199583 free inodes.

server3 `/data`: 167078457344 available bytes; 97.69% used; 225821888 free inodes.

server3 `/tmp`: 85898981376 available bytes; 95.21% used; 114199583 free inodes.

server3 `/var/tmp`: 85898981376 available bytes; 95.21% used; 114199583 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105759440896 available bytes; 94.10% used; 114349082 free inodes.

server4 `/home`: 105759440896 available bytes; 94.10% used; 114349082 free inodes.

server4 `/data`: 319660105728 available bytes; 95.58% used; 225273407 free inodes.

server4 `/tmp`: 105759440896 available bytes; 94.10% used; 114349082 free inodes.

server4 `/var/tmp`: 105759440896 available bytes; 94.10% used; 114349082 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
