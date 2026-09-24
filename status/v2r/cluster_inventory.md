# V2R cluster inventory

2026-09-24T10:56:06.826065+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324380925952 available bytes; 81.90% used; 112489067 free inodes.

server1 `/home`: 324380925952 available bytes; 81.90% used; 112489067 free inodes.

server1 `/tmp`: 324380925952 available bytes; 81.90% used; 112489067 free inodes.

server1 `/var/tmp`: 324380925952 available bytes; 81.90% used; 112489067 free inodes.

server1 `/mnt/raid5`: 496844730368 available bytes; 97.72% used; 337694003 free inodes.
| server2 | True | ['6'] | [] | reference_compatible=False |

server2 `/`: 57698836480 available bytes; 96.78% used; 110430333 free inodes.

server2 `/home`: 57698836480 available bytes; 96.78% used; 110430333 free inodes.

server2 `/tmp`: 57698836480 available bytes; 96.78% used; 110430333 free inodes.

server2 `/var/tmp`: 57698836480 available bytes; 96.78% used; 110430333 free inodes.

server2 `/mnt/raid5`: 511998636032 available bytes; 96.46% used; 445174675 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 85784100864 available bytes; 95.21% used; 114197380 free inodes.

server3 `/home`: 85784100864 available bytes; 95.21% used; 114197380 free inodes.

server3 `/data`: 164061138944 available bytes; 97.73% used; 225817712 free inodes.

server3 `/tmp`: 85784100864 available bytes; 95.21% used; 114197380 free inodes.

server3 `/var/tmp`: 85784100864 available bytes; 95.21% used; 114197380 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105734922240 available bytes; 94.10% used; 114348935 free inodes.

server4 `/home`: 105734922240 available bytes; 94.10% used; 114348935 free inodes.

server4 `/data`: 132779728896 available bytes; 98.16% used; 225258266 free inodes.

server4 `/tmp`: 105734922240 available bytes; 94.10% used; 114348935 free inodes.

server4 `/var/tmp`: 105734922240 available bytes; 94.10% used; 114348935 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
