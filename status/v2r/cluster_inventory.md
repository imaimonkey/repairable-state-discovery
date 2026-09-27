# V2R cluster inventory

2026-09-27T02:31:48.762221+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['2', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 315078111232 available bytes; 82.42% used; 112443393 free inodes.

server1 `/home`: 315078111232 available bytes; 82.42% used; 112443393 free inodes.

server1 `/tmp`: 315078111232 available bytes; 82.42% used; 112443393 free inodes.

server1 `/var/tmp`: 315078111232 available bytes; 82.42% used; 112443393 free inodes.

server1 `/mnt/raid5`: 637262413824 available bytes; 97.08% used; 337401648 free inodes.
| server2 | True | [] | [] |

server2 `/`: 17635000320 available bytes; 99.02% used; 110365004 free inodes.

server2 `/home`: 17635000320 available bytes; 99.02% used; 110365004 free inodes.

server2 `/tmp`: 17635000320 available bytes; 99.02% used; 110365004 free inodes.

server2 `/var/tmp`: 17635000320 available bytes; 99.02% used; 110365004 free inodes.

server2 `/mnt/raid5`: 580910956544 available bytes; 95.99% used; 444884606 free inodes.
| server3 | True | [] | [] |

server3 `/`: 78708817920 available bytes; 95.61% used; 114062953 free inodes.

server3 `/home`: 78708817920 available bytes; 95.61% used; 114062953 free inodes.

server3 `/data`: 1337688059904 available bytes; 81.51% used; 225762345 free inodes.

server3 `/tmp`: 78708817920 available bytes; 95.61% used; 114062953 free inodes.

server3 `/var/tmp`: 78708817920 available bytes; 95.61% used; 114062953 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 111036342272 available bytes; 93.80% used; 114373252 free inodes.

server4 `/home`: 111036342272 available bytes; 93.80% used; 114373252 free inodes.

server4 `/data`: 400294600704 available bytes; 94.47% used; 224781592 free inodes.

server4 `/tmp`: 111036342272 available bytes; 93.80% used; 114373252 free inodes.

server4 `/var/tmp`: 111036342272 available bytes; 93.80% used; 114373252 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
