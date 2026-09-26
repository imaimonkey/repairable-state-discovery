# V2R cluster inventory

2026-09-26T11:16:45.222020+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318217129984 available bytes; 82.25% used; 112474824 free inodes.

server1 `/home`: 318217129984 available bytes; 82.25% used; 112474824 free inodes.

server1 `/tmp`: 318217129984 available bytes; 82.25% used; 112474824 free inodes.

server1 `/var/tmp`: 318217129984 available bytes; 82.25% used; 112474824 free inodes.

server1 `/mnt/raid5`: 218729107456 available bytes; 99.00% used; 337538142 free inodes.
| server2 | True | [] | [] |

server2 `/`: 19844661248 available bytes; 98.89% used; 110384878 free inodes.

server2 `/home`: 19844661248 available bytes; 98.89% used; 110384878 free inodes.

server2 `/tmp`: 19844661248 available bytes; 98.89% used; 110384878 free inodes.

server2 `/var/tmp`: 19844661248 available bytes; 98.89% used; 110384878 free inodes.

server2 `/mnt/raid5`: 241833615360 available bytes; 98.33% used; 444978629 free inodes.
| server3 | True | [] | [] |

server3 `/`: 82648674304 available bytes; 95.39% used; 114110811 free inodes.

server3 `/home`: 82648674304 available bytes; 95.39% used; 114110811 free inodes.

server3 `/data`: 123570966528 available bytes; 98.29% used; 225825743 free inodes.

server3 `/tmp`: 82648674304 available bytes; 95.39% used; 114110811 free inodes.

server3 `/var/tmp`: 82648674304 available bytes; 95.39% used; 114110811 free inodes.
| server4 | True | ['0', '3', '5', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105925099520 available bytes; 94.09% used; 114347941 free inodes.

server4 `/home`: 105925099520 available bytes; 94.09% used; 114347941 free inodes.

server4 `/data`: 88799854592 available bytes; 98.77% used; 224880356 free inodes.

server4 `/tmp`: 105925099520 available bytes; 94.09% used; 114347941 free inodes.

server4 `/var/tmp`: 105925099520 available bytes; 94.09% used; 114347941 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
