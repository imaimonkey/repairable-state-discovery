# V2R cluster inventory

2026-09-24T10:54:40.326740+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 324382412800 available bytes; 81.90% used; 112489070 free inodes.

server1 `/home`: 324382412800 available bytes; 81.90% used; 112489070 free inodes.

server1 `/tmp`: 324382412800 available bytes; 81.90% used; 112489070 free inodes.

server1 `/var/tmp`: 324382412800 available bytes; 81.90% used; 112489070 free inodes.

server1 `/mnt/raid5`: 498873757696 available bytes; 97.71% used; 337694201 free inodes.
| server2 | True | ['6'] | [] |

server2 `/`: 57701490688 available bytes; 96.78% used; 110430343 free inodes.

server2 `/home`: 57701490688 available bytes; 96.78% used; 110430343 free inodes.

server2 `/tmp`: 57701490688 available bytes; 96.78% used; 110430343 free inodes.

server2 `/var/tmp`: 57701490688 available bytes; 96.78% used; 110430343 free inodes.

server2 `/mnt/raid5`: 512044965888 available bytes; 96.46% used; 445174825 free inodes.
| server3 | True | [] | [] |

server3 `/`: 85786349568 available bytes; 95.21% used; 114197498 free inodes.

server3 `/home`: 85786349568 available bytes; 95.21% used; 114197498 free inodes.

server3 `/data`: 164071424000 available bytes; 97.73% used; 225817743 free inodes.

server3 `/tmp`: 85786349568 available bytes; 95.21% used; 114197498 free inodes.

server3 `/var/tmp`: 85786349568 available bytes; 95.21% used; 114197498 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105735057408 available bytes; 94.10% used; 114348939 free inodes.

server4 `/home`: 105735057408 available bytes; 94.10% used; 114348939 free inodes.

server4 `/data`: 132782235648 available bytes; 98.16% used; 225258288 free inodes.

server4 `/tmp`: 105735057408 available bytes; 94.10% used; 114348939 free inodes.

server4 `/var/tmp`: 105735057408 available bytes; 94.10% used; 114348939 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
