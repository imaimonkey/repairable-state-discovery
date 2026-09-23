# V2R cluster inventory

2026-09-23T19:30:56.481990+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['4', '7'] | ['/tmp', '/var/tmp', '/mnt/raid5'] | reference_compatible=False |

server1 `/`: 325751582720 available bytes; 81.83% used; 112501874 free inodes.

server1 `/home`: 325751582720 available bytes; 81.83% used; 112501874 free inodes.

server1 `/tmp`: 325751582720 available bytes; 81.83% used; 112501874 free inodes.

server1 `/var/tmp`: 325751582720 available bytes; 81.83% used; 112501874 free inodes.

server1 `/mnt/raid5`: 1389199138816 available bytes; 93.63% used; 337741343 free inodes.
| server2 | True | ['6', '7'] | [] | reference_compatible=False |

server2 `/`: 41329266688 available bytes; 97.69% used; 110435438 free inodes.

server2 `/home`: 41329266688 available bytes; 97.69% used; 110435438 free inodes.

server2 `/tmp`: 41329266688 available bytes; 97.69% used; 110435438 free inodes.

server2 `/var/tmp`: 41329266688 available bytes; 97.69% used; 110435438 free inodes.

server2 `/mnt/raid5`: 543137599488 available bytes; 96.25% used; 445212540 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 293136318464 available bytes; 83.64% used; 114213280 free inodes.

server3 `/home`: 293136318464 available bytes; 83.64% used; 114213280 free inodes.

server3 `/data`: 52737691648 available bytes; 99.27% used; 225845191 free inodes.

server3 `/tmp`: 293136318464 available bytes; 83.64% used; 114213280 free inodes.

server3 `/var/tmp`: 293136318464 available bytes; 83.64% used; 114213280 free inodes.
| server4 | True | ['0', '1', '2', '3', '4', '5', '6'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 106529894400 available bytes; 94.06% used; 114356236 free inodes.

server4 `/home`: 106529894400 available bytes; 94.06% used; 114356236 free inodes.

server4 `/data`: 1773568 available bytes; 100.00% used; 225457640 free inodes.

server4 `/tmp`: 106529894400 available bytes; 94.06% used; 114356236 free inodes.

server4 `/var/tmp`: 106529894400 available bytes; 94.06% used; 114356236 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
