# V2R cluster inventory

2026-09-25T05:35:15.025858+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318873395200 available bytes; 82.21% used; 112480329 free inodes.

server1 `/home`: 318873395200 available bytes; 82.21% used; 112480329 free inodes.

server1 `/tmp`: 318873395200 available bytes; 82.21% used; 112480329 free inodes.

server1 `/var/tmp`: 318873395200 available bytes; 82.21% used; 112480329 free inodes.

server1 `/mnt/raid5`: 408478240768 available bytes; 98.13% used; 337567647 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22919876608 available bytes; 98.72% used; 110410443 free inodes.

server2 `/home`: 22919876608 available bytes; 98.72% used; 110410443 free inodes.

server2 `/tmp`: 22919876608 available bytes; 98.72% used; 110410443 free inodes.

server2 `/var/tmp`: 22919876608 available bytes; 98.72% used; 110410443 free inodes.

server2 `/mnt/raid5`: 468867297280 available bytes; 96.76% used; 445103148 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84313927680 available bytes; 95.29% used; 114156039 free inodes.

server3 `/home`: 84313927680 available bytes; 95.29% used; 114156039 free inodes.

server3 `/data`: 142778335232 available bytes; 98.03% used; 225814728 free inodes.

server3 `/tmp`: 84313927680 available bytes; 95.29% used; 114156039 free inodes.

server3 `/var/tmp`: 84313927680 available bytes; 95.29% used; 114156039 free inodes.
| server4 | True | ['3'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105649868800 available bytes; 94.10% used; 114350392 free inodes.

server4 `/home`: 105649868800 available bytes; 94.10% used; 114350392 free inodes.

server4 `/data`: 26386345984 available bytes; 99.64% used; 224967531 free inodes.

server4 `/tmp`: 105649868800 available bytes; 94.10% used; 114350392 free inodes.

server4 `/var/tmp`: 105649868800 available bytes; 94.10% used; 114350392 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
