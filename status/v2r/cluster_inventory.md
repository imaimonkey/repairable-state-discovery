# V2R cluster inventory

2026-09-23T23:00:54.743883+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['6', '7'] | ['/tmp', '/var/tmp', '/mnt/raid5'] | reference_compatible=False |

server1 `/`: 325744050176 available bytes; 81.83% used; 112501695 free inodes.

server1 `/home`: 325744050176 available bytes; 81.83% used; 112501695 free inodes.

server1 `/tmp`: 325744050176 available bytes; 81.83% used; 112501695 free inodes.

server1 `/var/tmp`: 325744050176 available bytes; 81.83% used; 112501695 free inodes.

server1 `/mnt/raid5`: 1387997630464 available bytes; 93.63% used; 337739796 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 41060773888 available bytes; 97.71% used; 110432611 free inodes.

server2 `/home`: 41060773888 available bytes; 97.71% used; 110432611 free inodes.

server2 `/tmp`: 41060773888 available bytes; 97.71% used; 110432611 free inodes.

server2 `/var/tmp`: 41060773888 available bytes; 97.71% used; 110432611 free inodes.

server2 `/mnt/raid5`: 535358976000 available bytes; 96.30% used; 445205869 free inodes.
| server3 | True | ['3'] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 292835581952 available bytes; 83.66% used; 114213845 free inodes.

server3 `/home`: 292835581952 available bytes; 83.66% used; 114213845 free inodes.

server3 `/data`: 82347450368 available bytes; 98.86% used; 225846653 free inodes.

server3 `/tmp`: 292835581952 available bytes; 83.66% used; 114213845 free inodes.

server3 `/var/tmp`: 292835581952 available bytes; 83.66% used; 114213845 free inodes.
| server4 | True | ['3', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 106295099392 available bytes; 94.07% used; 114353419 free inodes.

server4 `/home`: 106295099392 available bytes; 94.07% used; 114353419 free inodes.

server4 `/data`: 300075724800 available bytes; 95.85% used; 225431923 free inodes.

server4 `/tmp`: 106295099392 available bytes; 94.07% used; 114353419 free inodes.

server4 `/var/tmp`: 106295099392 available bytes; 94.07% used; 114353419 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
