# V2R cluster inventory

2026-09-25T21:15:53.539632+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['4', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318704508928 available bytes; 82.22% used; 112476315 free inodes.

server1 `/home`: 318704508928 available bytes; 82.22% used; 112476315 free inodes.

server1 `/tmp`: 318704508928 available bytes; 82.22% used; 112476315 free inodes.

server1 `/var/tmp`: 318704508928 available bytes; 82.22% used; 112476315 free inodes.

server1 `/mnt/raid5`: 368329744384 available bytes; 98.31% used; 337539400 free inodes.
| server2 | True | ['6'] | [] | reference_compatible=False |

server2 `/`: 22888886272 available bytes; 98.72% used; 110405686 free inodes.

server2 `/home`: 22888886272 available bytes; 98.72% used; 110405686 free inodes.

server2 `/tmp`: 22888886272 available bytes; 98.72% used; 110405686 free inodes.

server2 `/var/tmp`: 22888886272 available bytes; 98.72% used; 110405686 free inodes.

server2 `/mnt/raid5`: 301424431104 available bytes; 97.92% used; 445055434 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84368007168 available bytes; 95.29% used; 114152630 free inodes.

server3 `/home`: 84368007168 available bytes; 95.29% used; 114152630 free inodes.

server3 `/data`: 125903282176 available bytes; 98.26% used; 225807233 free inodes.

server3 `/tmp`: 84368007168 available bytes; 95.29% used; 114152630 free inodes.

server3 `/var/tmp`: 84368007168 available bytes; 95.29% used; 114152630 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105389469696 available bytes; 94.12% used; 114347331 free inodes.

server4 `/home`: 105389469696 available bytes; 94.12% used; 114347331 free inodes.

server4 `/data`: 217865801728 available bytes; 96.99% used; 224920460 free inodes.

server4 `/tmp`: 105389469696 available bytes; 94.12% used; 114347331 free inodes.

server4 `/var/tmp`: 105389469696 available bytes; 94.12% used; 114347331 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
