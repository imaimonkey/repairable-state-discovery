# V2R cluster inventory

2026-09-27T11:08:57.149764+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['2', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 304695324672 available bytes; 83.00% used; 112401745 free inodes.

server1 `/home`: 304695324672 available bytes; 83.00% used; 112401745 free inodes.

server1 `/tmp`: 304695324672 available bytes; 83.00% used; 112401745 free inodes.

server1 `/var/tmp`: 304695324672 available bytes; 83.00% used; 112401745 free inodes.

server1 `/mnt/raid5`: 635400491008 available bytes; 97.09% used; 337424416 free inodes.
| server2 | True | ['1', '2', '7'] | [] | reference_compatible=False |

server2 `/`: 16444305408 available bytes; 99.08% used; 110353739 free inodes.

server2 `/home`: 16444305408 available bytes; 99.08% used; 110353739 free inodes.

server2 `/tmp`: 16444305408 available bytes; 99.08% used; 110353739 free inodes.

server2 `/var/tmp`: 16444305408 available bytes; 99.08% used; 110353739 free inodes.

server2 `/mnt/raid5`: 570660442112 available bytes; 96.06% used; 444737482 free inodes.
| server3 | True | ['0'] | [] | reference_compatible=True |

server3 `/`: 78544605184 available bytes; 95.62% used; 114062811 free inodes.

server3 `/home`: 78544605184 available bytes; 95.62% used; 114062811 free inodes.

server3 `/data`: 1332002004992 available bytes; 81.59% used; 225760214 free inodes.

server3 `/tmp`: 78544605184 available bytes; 95.62% used; 114062811 free inodes.

server3 `/var/tmp`: 78544605184 available bytes; 95.62% used; 114062811 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 107091124224 available bytes; 94.02% used; 114372757 free inodes.

server4 `/home`: 107091091456 available bytes; 94.02% used; 114372757 free inodes.

server4 `/data`: 361148243968 available bytes; 95.01% used; 224749162 free inodes.

server4 `/tmp`: 107091042304 available bytes; 94.02% used; 114372757 free inodes.

server4 `/var/tmp`: 107091013632 available bytes; 94.02% used; 114372757 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
