# V2R cluster inventory

2026-09-23T21:18:09.858382+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['6', '7'] | ['/tmp', '/var/tmp', '/mnt/raid5'] |

server1 `/`: 325720977408 available bytes; 81.83% used; 112501440 free inodes.

server1 `/home`: 325720977408 available bytes; 81.83% used; 112501440 free inodes.

server1 `/tmp`: 325720977408 available bytes; 81.83% used; 112501440 free inodes.

server1 `/var/tmp`: 325720977408 available bytes; 81.83% used; 112501440 free inodes.

server1 `/mnt/raid5`: 1388134543360 available bytes; 93.63% used; 337739973 free inodes.
| server2 | True | [] | [] |

server2 `/`: 41112477696 available bytes; 97.71% used; 110432694 free inodes.

server2 `/home`: 41112477696 available bytes; 97.71% used; 110432694 free inodes.

server2 `/tmp`: 41112477696 available bytes; 97.71% used; 110432694 free inodes.

server2 `/var/tmp`: 41112477696 available bytes; 97.71% used; 110432694 free inodes.

server2 `/mnt/raid5`: 538894508032 available bytes; 96.28% used; 445209232 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] |

server3 `/`: 292819300352 available bytes; 83.66% used; 114203353 free inodes.

server3 `/home`: 292819300352 available bytes; 83.66% used; 114203353 free inodes.

server3 `/data`: 52305342464 available bytes; 99.28% used; 225849326 free inodes.

server3 `/tmp`: 292819300352 available bytes; 83.66% used; 114203353 free inodes.

server3 `/var/tmp`: 292819300352 available bytes; 83.66% used; 114203353 free inodes.
| server4 | True | ['2', '3', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 106489307136 available bytes; 94.06% used; 114356029 free inodes.

server4 `/home`: 106489307136 available bytes; 94.06% used; 114356029 free inodes.

server4 `/data`: 300425261056 available bytes; 95.85% used; 225453353 free inodes.

server4 `/tmp`: 106489307136 available bytes; 94.06% used; 114356029 free inodes.

server4 `/var/tmp`: 106489307136 available bytes; 94.06% used; 114356029 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
