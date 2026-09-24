# V2R cluster inventory

2026-09-24T09:44:47.939255+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 324451110912 available bytes; 81.90% used; 112489702 free inodes.

server1 `/home`: 324451110912 available bytes; 81.90% used; 112489702 free inodes.

server1 `/tmp`: 324451110912 available bytes; 81.90% used; 112489702 free inodes.

server1 `/var/tmp`: 324451110912 available bytes; 81.90% used; 112489702 free inodes.

server1 `/mnt/raid5`: 501794455552 available bytes; 97.70% used; 337711574 free inodes.
| server2 | True | [] | [] |

server2 `/`: 57757372416 available bytes; 96.78% used; 110430779 free inodes.

server2 `/home`: 57757372416 available bytes; 96.78% used; 110430779 free inodes.

server2 `/tmp`: 57757372416 available bytes; 96.78% used; 110430779 free inodes.

server2 `/var/tmp`: 57757372416 available bytes; 96.78% used; 110430779 free inodes.

server2 `/mnt/raid5`: 514141818880 available bytes; 96.45% used; 445176976 free inodes.
| server3 | True | [] | [] |

server3 `/`: 85832159232 available bytes; 95.21% used; 114199422 free inodes.

server3 `/home`: 85832159232 available bytes; 95.21% used; 114199422 free inodes.

server3 `/data`: 165675581440 available bytes; 97.71% used; 225819899 free inodes.

server3 `/tmp`: 85832159232 available bytes; 95.21% used; 114199422 free inodes.

server3 `/var/tmp`: 85832159232 available bytes; 95.21% used; 114199422 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105748652032 available bytes; 94.10% used; 114349034 free inodes.

server4 `/home`: 105748652032 available bytes; 94.10% used; 114349034 free inodes.

server4 `/data`: 154563125248 available bytes; 97.86% used; 225273218 free inodes.

server4 `/tmp`: 105748652032 available bytes; 94.10% used; 114349034 free inodes.

server4 `/var/tmp`: 105748652032 available bytes; 94.10% used; 114349034 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
