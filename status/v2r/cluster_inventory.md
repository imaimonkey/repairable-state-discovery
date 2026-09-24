# V2R cluster inventory

2026-09-24T19:44:40.987311+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 323989053440 available bytes; 81.93% used; 112481462 free inodes.

server1 `/home`: 323989053440 available bytes; 81.93% used; 112481462 free inodes.

server1 `/tmp`: 323989053440 available bytes; 81.93% used; 112481462 free inodes.

server1 `/var/tmp`: 323989053440 available bytes; 81.93% used; 112481462 free inodes.

server1 `/mnt/raid5`: 415588663296 available bytes; 98.09% used; 337630668 free inodes.
| server2 | True | [] | [] |

server2 `/`: 44744028160 available bytes; 97.50% used; 110411693 free inodes.

server2 `/home`: 44744028160 available bytes; 97.50% used; 110411693 free inodes.

server2 `/tmp`: 44744028160 available bytes; 97.50% used; 110411693 free inodes.

server2 `/var/tmp`: 44744028160 available bytes; 97.50% used; 110411693 free inodes.

server2 `/mnt/raid5`: 494413918208 available bytes; 96.58% used; 445158280 free inodes.
| server3 | True | ['1'] | [] |

server3 `/`: 84400181248 available bytes; 95.29% used; 114156139 free inodes.

server3 `/home`: 84400181248 available bytes; 95.29% used; 114156139 free inodes.

server3 `/data`: 152132378624 available bytes; 97.90% used; 225799243 free inodes.

server3 `/tmp`: 84400181248 available bytes; 95.29% used; 114156139 free inodes.

server3 `/var/tmp`: 84400181248 available bytes; 95.29% used; 114156139 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105642311680 available bytes; 94.10% used; 114348430 free inodes.

server4 `/home`: 105642311680 available bytes; 94.10% used; 114348430 free inodes.

server4 `/data`: 89852215296 available bytes; 98.76% used; 225266561 free inodes.

server4 `/tmp`: 105642311680 available bytes; 94.10% used; 114348430 free inodes.

server4 `/var/tmp`: 105642311680 available bytes; 94.10% used; 114348430 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
