# V2R cluster inventory

2026-09-24T11:02:26.339279+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 324375379968 available bytes; 81.90% used; 112489022 free inodes.

server1 `/home`: 324375379968 available bytes; 81.90% used; 112489022 free inodes.

server1 `/tmp`: 324375379968 available bytes; 81.90% used; 112489022 free inodes.

server1 `/var/tmp`: 324375379968 available bytes; 81.90% used; 112489022 free inodes.

server1 `/mnt/raid5`: 486949998592 available bytes; 97.77% used; 337693176 free inodes.
| server2 | True | ['6'] | [] |

server2 `/`: 57696882688 available bytes; 96.78% used; 110430269 free inodes.

server2 `/home`: 57696882688 available bytes; 96.78% used; 110430269 free inodes.

server2 `/tmp`: 57696882688 available bytes; 96.78% used; 110430269 free inodes.

server2 `/var/tmp`: 57696882688 available bytes; 96.78% used; 110430269 free inodes.

server2 `/mnt/raid5`: 511774064640 available bytes; 96.46% used; 445174461 free inodes.
| server3 | True | [] | [] |

server3 `/`: 85545775104 available bytes; 95.23% used; 114190342 free inodes.

server3 `/home`: 85545775104 available bytes; 95.23% used; 114190342 free inodes.

server3 `/data`: 164004585472 available bytes; 97.73% used; 225817560 free inodes.

server3 `/tmp`: 85545775104 available bytes; 95.23% used; 114190342 free inodes.

server3 `/var/tmp`: 85545775104 available bytes; 95.23% used; 114190342 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105734631424 available bytes; 94.10% used; 114348929 free inodes.

server4 `/home`: 105734631424 available bytes; 94.10% used; 114348929 free inodes.

server4 `/data`: 129614045184 available bytes; 98.21% used; 225258242 free inodes.

server4 `/tmp`: 105734631424 available bytes; 94.10% used; 114348929 free inodes.

server4 `/var/tmp`: 105734631424 available bytes; 94.10% used; 114348929 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
