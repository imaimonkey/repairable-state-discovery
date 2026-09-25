# V2R cluster inventory

2026-09-25T19:55:11.025857+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318713171968 available bytes; 82.22% used; 112476337 free inodes.

server1 `/home`: 318713171968 available bytes; 82.22% used; 112476337 free inodes.

server1 `/tmp`: 318713171968 available bytes; 82.22% used; 112476337 free inodes.

server1 `/var/tmp`: 318713171968 available bytes; 82.22% used; 112476337 free inodes.

server1 `/mnt/raid5`: 370818768896 available bytes; 98.30% used; 337540661 free inodes.
| server2 | True | ['2', '3', '4', '5', '6'] | [] |

server2 `/`: 23094706176 available bytes; 98.71% used; 110407938 free inodes.

server2 `/home`: 23094706176 available bytes; 98.71% used; 110407938 free inodes.

server2 `/tmp`: 23094706176 available bytes; 98.71% used; 110407938 free inodes.

server2 `/var/tmp`: 23094706176 available bytes; 98.71% used; 110407938 free inodes.

server2 `/mnt/raid5`: 310796980224 available bytes; 97.85% used; 445063405 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84381081600 available bytes; 95.29% used; 114152630 free inodes.

server3 `/home`: 84381081600 available bytes; 95.29% used; 114152630 free inodes.

server3 `/data`: 128246562816 available bytes; 98.23% used; 225808647 free inodes.

server3 `/tmp`: 84381081600 available bytes; 95.29% used; 114152630 free inodes.

server3 `/var/tmp`: 84381081600 available bytes; 95.29% used; 114152630 free inodes.
| server4 | True | ['3', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105673940992 available bytes; 94.10% used; 114349572 free inodes.

server4 `/home`: 105673940992 available bytes; 94.10% used; 114349572 free inodes.

server4 `/data`: 229443158016 available bytes; 96.83% used; 224929229 free inodes.

server4 `/tmp`: 105673940992 available bytes; 94.10% used; 114349572 free inodes.

server4 `/var/tmp`: 105673940992 available bytes; 94.10% used; 114349572 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
