# V2R cluster inventory

2026-09-23T13:19:03.143678+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | False | [] | [] |
| server2 | True | ['6', '7'] | [] |

server2 `/`: 41397960704 available bytes; 97.69% used; 110435599 free inodes.

server2 `/home`: 41397960704 available bytes; 97.69% used; 110435599 free inodes.

server2 `/tmp`: 41397960704 available bytes; 97.69% used; 110435599 free inodes.

server2 `/var/tmp`: 41397960704 available bytes; 97.69% used; 110435599 free inodes.

server2 `/mnt/raid5`: 555884146688 available bytes; 96.16% used; 445227974 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] |

server3 `/`: 378149666816 available bytes; 78.90% used; 114321080 free inodes.

server3 `/home`: 378149666816 available bytes; 78.90% used; 114321080 free inodes.

server3 `/data`: 134798323712 available bytes; 98.14% used; 225862139 free inodes.

server3 `/tmp`: 378149666816 available bytes; 78.90% used; 114321080 free inodes.

server3 `/var/tmp`: 378149666816 available bytes; 78.90% used; 114321080 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 111677079552 available bytes; 93.77% used; 114378480 free inodes.

server4 `/home`: 111677079552 available bytes; 93.77% used; 114378480 free inodes.

server4 `/data`: 48449552384 available bytes; 99.33% used; 225439894 free inodes.

server4 `/tmp`: 111677079552 available bytes; 93.77% used; 114378480 free inodes.

server4 `/var/tmp`: 111677079552 available bytes; 93.77% used; 114378480 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
