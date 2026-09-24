# V2R cluster inventory

2026-09-24T17:52:19.601322+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324006039552 available bytes; 81.92% used; 112481426 free inodes.

server1 `/home`: 324006039552 available bytes; 81.92% used; 112481426 free inodes.

server1 `/tmp`: 324006039552 available bytes; 81.92% used; 112481426 free inodes.

server1 `/var/tmp`: 324006039552 available bytes; 81.92% used; 112481426 free inodes.

server1 `/mnt/raid5`: 416395776000 available bytes; 98.09% used; 337643788 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 56901427200 available bytes; 96.83% used; 110412338 free inodes.

server2 `/home`: 56901427200 available bytes; 96.83% used; 110412338 free inodes.

server2 `/tmp`: 56901427200 available bytes; 96.83% used; 110412338 free inodes.

server2 `/var/tmp`: 56901427200 available bytes; 96.83% used; 110412338 free inodes.

server2 `/mnt/raid5`: 498186059776 available bytes; 96.56% used; 445161816 free inodes.
| server3 | True | ['1'] | [] | reference_compatible=True |

server3 `/`: 84408045568 available bytes; 95.29% used; 114156134 free inodes.

server3 `/home`: 84408045568 available bytes; 95.29% used; 114156134 free inodes.

server3 `/data`: 151873695744 available bytes; 97.90% used; 225786383 free inodes.

server3 `/tmp`: 84408045568 available bytes; 95.29% used; 114156134 free inodes.

server3 `/var/tmp`: 84408045568 available bytes; 95.29% used; 114156134 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105672298496 available bytes; 94.10% used; 114348541 free inodes.

server4 `/home`: 105672298496 available bytes; 94.10% used; 114348541 free inodes.

server4 `/data`: 88697511936 available bytes; 98.77% used; 225253580 free inodes.

server4 `/tmp`: 105672298496 available bytes; 94.10% used; 114348541 free inodes.

server4 `/var/tmp`: 105672298496 available bytes; 94.10% used; 114348541 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
