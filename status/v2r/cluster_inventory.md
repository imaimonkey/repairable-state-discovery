# V2R cluster inventory

2026-09-23T10:53:04.721784+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | False | [] | [] |
| server2 | True | ['7'] | [] |

server2 `/`: 41851899904 available bytes; 97.67% used; 110436712 free inodes.

server2 `/home`: 41851899904 available bytes; 97.67% used; 110436712 free inodes.

server2 `/tmp`: 41851899904 available bytes; 97.67% used; 110436712 free inodes.

server2 `/var/tmp`: 41851899904 available bytes; 97.67% used; 110436712 free inodes.

server2 `/mnt/raid5`: 547795763200 available bytes; 96.21% used; 445239293 free inodes.
| server3 | True | ['1', '3'] | ['/tmp', '/var/tmp'] |

server3 `/`: 380807933952 available bytes; 78.75% used; 114373577 free inodes.

server3 `/home`: 380807933952 available bytes; 78.75% used; 114373577 free inodes.

server3 `/data`: 140591243264 available bytes; 98.06% used; 225871658 free inodes.

server3 `/tmp`: 380807933952 available bytes; 78.75% used; 114373577 free inodes.

server3 `/var/tmp`: 380807933952 available bytes; 78.75% used; 114373577 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 111605989376 available bytes; 93.77% used; 114379017 free inodes.

server4 `/home`: 111605989376 available bytes; 93.77% used; 114379017 free inodes.

server4 `/data`: 68317777920 available bytes; 99.06% used; 225405143 free inodes.

server4 `/tmp`: 111605989376 available bytes; 93.77% used; 114379017 free inodes.

server4 `/var/tmp`: 111605989376 available bytes; 93.77% used; 114379017 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
