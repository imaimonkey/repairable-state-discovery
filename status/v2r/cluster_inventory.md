# V2R cluster inventory

2026-09-24T10:14:11.900387+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324421783552 available bytes; 81.90% used; 112489411 free inodes.

server1 `/home`: 324421783552 available bytes; 81.90% used; 112489411 free inodes.

server1 `/tmp`: 324421783552 available bytes; 81.90% used; 112489411 free inodes.

server1 `/var/tmp`: 324421783552 available bytes; 81.90% used; 112489411 free inodes.

server1 `/mnt/raid5`: 500652040192 available bytes; 97.70% used; 337699709 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 57743343616 available bytes; 96.78% used; 110430701 free inodes.

server2 `/home`: 57743343616 available bytes; 96.78% used; 110430701 free inodes.

server2 `/tmp`: 57743343616 available bytes; 96.78% used; 110430701 free inodes.

server2 `/var/tmp`: 57743343616 available bytes; 96.78% used; 110430701 free inodes.

server2 `/mnt/raid5`: 513217585152 available bytes; 96.45% used; 445175934 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 85366951936 available bytes; 95.24% used; 114173519 free inodes.

server3 `/home`: 85366951936 available bytes; 95.24% used; 114173519 free inodes.

server3 `/data`: 164413353984 available bytes; 97.73% used; 225818977 free inodes.

server3 `/tmp`: 85366951936 available bytes; 95.24% used; 114173519 free inodes.

server3 `/var/tmp`: 85366951936 available bytes; 95.24% used; 114173519 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105747357696 available bytes; 94.10% used; 114349000 free inodes.

server4 `/home`: 105747357696 available bytes; 94.10% used; 114349000 free inodes.

server4 `/data`: 153489854464 available bytes; 97.88% used; 225258410 free inodes.

server4 `/tmp`: 105747357696 available bytes; 94.10% used; 114349000 free inodes.

server4 `/var/tmp`: 105747357696 available bytes; 94.10% used; 114349000 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
