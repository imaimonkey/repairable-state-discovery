# V2R cluster inventory

2026-09-25T06:30:13.521529+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318879891456 available bytes; 82.21% used; 112480350 free inodes.

server1 `/home`: 318879891456 available bytes; 82.21% used; 112480350 free inodes.

server1 `/tmp`: 318879891456 available bytes; 82.21% used; 112480350 free inodes.

server1 `/var/tmp`: 318879891456 available bytes; 82.21% used; 112480350 free inodes.

server1 `/mnt/raid5`: 399811420160 available bytes; 98.17% used; 337561443 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 22896476160 available bytes; 98.72% used; 110410518 free inodes.

server2 `/home`: 22896476160 available bytes; 98.72% used; 110410518 free inodes.

server2 `/tmp`: 22896476160 available bytes; 98.72% used; 110410518 free inodes.

server2 `/var/tmp`: 22896476160 available bytes; 98.72% used; 110410518 free inodes.

server2 `/mnt/raid5`: 370538975232 available bytes; 97.44% used; 445099519 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84314382336 available bytes; 95.29% used; 114156029 free inodes.

server3 `/home`: 84314382336 available bytes; 95.29% used; 114156029 free inodes.

server3 `/data`: 142534594560 available bytes; 98.03% used; 225813788 free inodes.

server3 `/tmp`: 84314382336 available bytes; 95.29% used; 114156029 free inodes.

server3 `/var/tmp`: 84314382336 available bytes; 95.29% used; 114156029 free inodes.
| server4 | True | ['3'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105648205824 available bytes; 94.10% used; 114350390 free inodes.

server4 `/home`: 105648205824 available bytes; 94.10% used; 114350390 free inodes.

server4 `/data`: 253576278016 available bytes; 96.50% used; 225020709 free inodes.

server4 `/tmp`: 105648205824 available bytes; 94.10% used; 114350390 free inodes.

server4 `/var/tmp`: 105648205824 available bytes; 94.10% used; 114350390 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
