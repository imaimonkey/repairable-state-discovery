# V2R cluster inventory

2026-09-26T09:35:55.227242+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318627061760 available bytes; 82.22% used; 112475085 free inodes.

server1 `/home`: 318627061760 available bytes; 82.22% used; 112475085 free inodes.

server1 `/tmp`: 318627061760 available bytes; 82.22% used; 112475085 free inodes.

server1 `/var/tmp`: 318627061760 available bytes; 82.22% used; 112475085 free inodes.

server1 `/mnt/raid5`: 218959204352 available bytes; 99.00% used; 337538629 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22315581440 available bytes; 98.76% used; 110403896 free inodes.

server2 `/home`: 22315581440 available bytes; 98.76% used; 110403896 free inodes.

server2 `/tmp`: 22315581440 available bytes; 98.76% used; 110403896 free inodes.

server2 `/var/tmp`: 22315581440 available bytes; 98.76% used; 110403896 free inodes.

server2 `/mnt/raid5`: 254021328896 available bytes; 98.24% used; 445022722 free inodes.
| server3 | True | [] | [] |

server3 `/`: 82656829440 available bytes; 95.39% used; 114110791 free inodes.

server3 `/home`: 82656829440 available bytes; 95.39% used; 114110791 free inodes.

server3 `/data`: 123653902336 available bytes; 98.29% used; 225827732 free inodes.

server3 `/tmp`: 82656829440 available bytes; 95.39% used; 114110791 free inodes.

server3 `/var/tmp`: 82656829440 available bytes; 95.39% used; 114110791 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105942700032 available bytes; 94.09% used; 114348052 free inodes.

server4 `/home`: 105942700032 available bytes; 94.09% used; 114348052 free inodes.

server4 `/data`: 89282453504 available bytes; 98.77% used; 224882694 free inodes.

server4 `/tmp`: 105942700032 available bytes; 94.09% used; 114348052 free inodes.

server4 `/var/tmp`: 105942700032 available bytes; 94.09% used; 114348052 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
