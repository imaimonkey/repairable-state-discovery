# V2R cluster inventory

2026-09-23T19:47:10.749515+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['4', '7'] | ['/tmp', '/var/tmp', '/mnt/raid5'] | reference_compatible=False |

server1 `/`: 325749485568 available bytes; 81.83% used; 112501838 free inodes.

server1 `/home`: 325749485568 available bytes; 81.83% used; 112501838 free inodes.

server1 `/tmp`: 325749485568 available bytes; 81.83% used; 112501838 free inodes.

server1 `/var/tmp`: 325749485568 available bytes; 81.83% used; 112501838 free inodes.

server1 `/mnt/raid5`: 1389164896256 available bytes; 93.63% used; 337741292 free inodes.
| server2 | True | ['6', '7'] | [] | reference_compatible=False |

server2 `/`: 41322868736 available bytes; 97.69% used; 110435430 free inodes.

server2 `/home`: 41322868736 available bytes; 97.69% used; 110435430 free inodes.

server2 `/tmp`: 41322868736 available bytes; 97.69% used; 110435430 free inodes.

server2 `/var/tmp`: 41322868736 available bytes; 97.69% used; 110435430 free inodes.

server2 `/mnt/raid5`: 542547148800 available bytes; 96.25% used; 445211900 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 293691826176 available bytes; 83.61% used; 114247692 free inodes.

server3 `/home`: 293691826176 available bytes; 83.61% used; 114247692 free inodes.

server3 `/data`: 52717756416 available bytes; 99.27% used; 225844884 free inodes.

server3 `/tmp`: 293691826176 available bytes; 83.61% used; 114247692 free inodes.

server3 `/var/tmp`: 293691826176 available bytes; 83.61% used; 114247692 free inodes.
| server4 | True | ['0', '1', '2', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 106528907264 available bytes; 94.06% used; 114356236 free inodes.

server4 `/home`: 106528907264 available bytes; 94.06% used; 114356236 free inodes.

server4 `/data`: 0 available bytes; 100.00% used; 225457640 free inodes.

server4 `/tmp`: 106528907264 available bytes; 94.06% used; 114356236 free inodes.

server4 `/var/tmp`: 106528907264 available bytes; 94.06% used; 114356236 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
