# V2R cluster inventory

2026-09-23T19:01:00.513566+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['4', '7'] | ['/tmp', '/var/tmp', '/mnt/raid5'] |

server1 `/`: 331615821824 available bytes; 81.50% used; 112554817 free inodes.

server1 `/home`: 331615821824 available bytes; 81.50% used; 112554817 free inodes.

server1 `/tmp`: 331615821824 available bytes; 81.50% used; 112554817 free inodes.

server1 `/var/tmp`: 331615821824 available bytes; 81.50% used; 112554817 free inodes.

server1 `/mnt/raid5`: 1389253861376 available bytes; 93.63% used; 337741437 free inodes.
| server2 | True | ['6', '7'] | [] |

server2 `/`: 41339953152 available bytes; 97.69% used; 110435448 free inodes.

server2 `/home`: 41339953152 available bytes; 97.69% used; 110435448 free inodes.

server2 `/tmp`: 41339953152 available bytes; 97.69% used; 110435448 free inodes.

server2 `/var/tmp`: 41339953152 available bytes; 97.69% used; 110435448 free inodes.

server2 `/mnt/raid5`: 544014966784 available bytes; 96.24% used; 445213442 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] |

server3 `/`: 293879459840 available bytes; 83.60% used; 114251015 free inodes.

server3 `/home`: 293879459840 available bytes; 83.60% used; 114251015 free inodes.

server3 `/data`: 52808388608 available bytes; 99.27% used; 225846417 free inodes.

server3 `/tmp`: 293879459840 available bytes; 83.60% used; 114251015 free inodes.

server3 `/var/tmp`: 293879459840 available bytes; 83.60% used; 114251015 free inodes.
| server4 | True | ['0', '1', '2', '3', '4', '5', '6'] | ['/tmp', '/var/tmp'] |

server4 `/`: 106475859968 available bytes; 94.06% used; 114356235 free inodes.

server4 `/home`: 106475859968 available bytes; 94.06% used; 114356235 free inodes.

server4 `/data`: 0 available bytes; 100.00% used; 225457658 free inodes.

server4 `/tmp`: 106475859968 available bytes; 94.06% used; 114356235 free inodes.

server4 `/var/tmp`: 106475859968 available bytes; 94.06% used; 114356235 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
