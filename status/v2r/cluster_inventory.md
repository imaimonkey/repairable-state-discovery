# V2R cluster inventory

2026-09-23T23:17:49.800245+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['6', '7'] | ['/tmp', '/var/tmp', '/mnt/raid5'] | reference_compatible=False |

server1 `/`: 325664813056 available bytes; 81.83% used; 112501613 free inodes.

server1 `/home`: 325664813056 available bytes; 81.83% used; 112501613 free inodes.

server1 `/tmp`: 325664813056 available bytes; 81.83% used; 112501613 free inodes.

server1 `/var/tmp`: 325664813056 available bytes; 81.83% used; 112501613 free inodes.

server1 `/mnt/raid5`: 1387842617344 available bytes; 93.63% used; 337739851 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 41050009600 available bytes; 97.71% used; 110432606 free inodes.

server2 `/home`: 41050009600 available bytes; 97.71% used; 110432606 free inodes.

server2 `/tmp`: 41050009600 available bytes; 97.71% used; 110432606 free inodes.

server2 `/var/tmp`: 41050009600 available bytes; 97.71% used; 110432606 free inodes.

server2 `/mnt/raid5`: 534884601856 available bytes; 96.30% used; 445206106 free inodes.
| server3 | True | ['3'] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 292246896640 available bytes; 83.69% used; 114171235 free inodes.

server3 `/home`: 292246896640 available bytes; 83.69% used; 114171235 free inodes.

server3 `/data`: 82326593536 available bytes; 98.86% used; 225846000 free inodes.

server3 `/tmp`: 292246896640 available bytes; 83.69% used; 114171235 free inodes.

server3 `/var/tmp`: 292246896640 available bytes; 83.69% used; 114171235 free inodes.
| server4 | True | ['3', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 106256875520 available bytes; 94.07% used; 114352807 free inodes.

server4 `/home`: 106256875520 available bytes; 94.07% used; 114352807 free inodes.

server4 `/data`: 296208601088 available bytes; 95.91% used; 225428100 free inodes.

server4 `/tmp`: 106256875520 available bytes; 94.07% used; 114352807 free inodes.

server4 `/var/tmp`: 106256875520 available bytes; 94.07% used; 114352807 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
