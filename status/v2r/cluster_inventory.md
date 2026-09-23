# V2R cluster inventory

2026-09-23T20:29:10.513903+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['3', '4', '7'] | ['/tmp', '/var/tmp', '/mnt/raid5'] |

server1 `/`: 325735526400 available bytes; 81.83% used; 112501759 free inodes.

server1 `/home`: 325735526400 available bytes; 81.83% used; 112501759 free inodes.

server1 `/tmp`: 325735526400 available bytes; 81.83% used; 112501759 free inodes.

server1 `/var/tmp`: 325735526400 available bytes; 81.83% used; 112501759 free inodes.

server1 `/mnt/raid5`: 1388273270784 available bytes; 93.63% used; 337740958 free inodes.
| server2 | True | ['6', '7'] | [] |

server2 `/`: 41141293056 available bytes; 97.70% used; 110432809 free inodes.

server2 `/home`: 41141293056 available bytes; 97.70% used; 110432809 free inodes.

server2 `/tmp`: 41141293056 available bytes; 97.70% used; 110432809 free inodes.

server2 `/var/tmp`: 41141293056 available bytes; 97.70% used; 110432809 free inodes.

server2 `/mnt/raid5`: 539884802048 available bytes; 96.27% used; 445210862 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] |

server3 `/`: 292613062656 available bytes; 83.67% used; 114188379 free inodes.

server3 `/home`: 292613062656 available bytes; 83.67% used; 114188379 free inodes.

server3 `/data`: 52590800896 available bytes; 99.27% used; 225843402 free inodes.

server3 `/tmp`: 292613062656 available bytes; 83.67% used; 114188379 free inodes.

server3 `/var/tmp`: 292613062656 available bytes; 83.67% used; 114188379 free inodes.
| server4 | True | ['0', '1', '2', '3', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 106527485952 available bytes; 94.06% used; 114356174 free inodes.

server4 `/home`: 106527485952 available bytes; 94.06% used; 114356174 free inodes.

server4 `/data`: 1044480 available bytes; 100.00% used; 225457595 free inodes.

server4 `/tmp`: 106527485952 available bytes; 94.06% used; 114356174 free inodes.

server4 `/var/tmp`: 106527485952 available bytes; 94.06% used; 114356174 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
